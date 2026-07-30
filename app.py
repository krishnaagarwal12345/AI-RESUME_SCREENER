from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from groq import Groq
import fitz  # PyMuPDF
import os
import json
import time

# ============================================
# CONFIGURATION
# ===========================================

from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

if not GROQ_API_KEY:
    print("⚠️ WARNING: GROQ_API_KEY not set!")
else:
    print(f"✅ API Key loaded: {GROQ_API_KEY[:8]}...")



MODEL = "llama-3.3-70b-versatile"

# ============================================
# INITIALIZE
# ============================================
print("Starting AI Resume Screener...")
groq_client = Groq(api_key=GROQ_API_KEY)
print("Ready! ✅")

# ============================================
# FASTAPI APP
# ============================================
app = FastAPI(
    title="AI Resume Screener",
    description="Screen resumes against job descriptions using AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# ============================================
# STORAGE
# ============================================
screening_store = {
    "resume_text": None,
    "job_text": None,
    "resume_filename": None,
    "job_filename": None
}

# ============================================
# HELPER FUNCTIONS
# ============================================
def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """Extract text from PDF"""
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text.strip()

def extract_text_from_txt(content: bytes) -> str:
    """Extract text from TXT file"""
    return content.decode('utf-8', errors='ignore').strip()

def analyze_resume_and_job(resume_text: str, job_text: str) -> dict:
    """Use AI to analyze resume against job description"""

    prompt = f"""You are an expert HR professional and technical recruiter.
Analyze the resume against the job description and provide a detailed assessment.

RESUME:
{resume_text[:3000]}

JOB DESCRIPTION:
{job_text[:2000]}

Provide your analysis in this EXACT JSON format:
{{
    "match_score": <number between 0-100>,
    "summary": "<2-3 sentence overall assessment>",
    "matching_skills": [
        "<skill 1>",
        "<skill 2>",
        "<skill 3>"
    ],
    "missing_skills": [
        "<missing skill 1>",
        "<missing skill 2>",
        "<missing skill 3>"
    ],
    "strengths": [
        "<strength 1>",
        "<strength 2>",
        "<strength 3>"
    ],
    "improvements": [
        "<improvement suggestion 1>",
        "<improvement suggestion 2>",
        "<improvement suggestion 3>"
    ],
    "experience_match": "<Excellent/Good/Fair/Poor>",
    "recommendation": "<Strongly Recommend/Recommend/Consider/Not Recommended>"
}}

Return ONLY the JSON. No extra text. No markdown.
Be specific and accurate based on the actual content."""

    response = groq_client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    result_text = response.choices[0].message.content.strip()

    # Clean JSON
    if result_text.startswith("```"):
        result_text = result_text.split("```")[1]
        if result_text.startswith("json"):
            result_text = result_text[4:]

    return json.loads(result_text)

def get_improvement_suggestions(
    resume_text: str,
    job_text: str,
    analysis: dict
) -> str:
    """Get detailed improvement suggestions"""

    missing = ", ".join(analysis.get("missing_skills", []))

    prompt = f"""You are a career coach helping a candidate improve their resume.

The candidate is missing these skills for the job: {missing}

Job requires: {job_text[:1000]}

Give 3 specific, actionable suggestions to improve their profile.
Each suggestion should be practical and achievable.
Format as numbered list. Keep each point under 2 sentences."""

    response = groq_client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content

# ============================================
# REQUEST / RESPONSE MODELS
# ============================================
class ScreeningResponse(BaseModel):
    match_score: int
    summary: str
    matching_skills: list
    missing_skills: list
    strengths: list
    improvements: list
    experience_match: str
    recommendation: str
    detailed_suggestions: str
    time_taken: float

class UploadResponse(BaseModel):
    message: str
    filename: str
    text_length: int

# ============================================
# ENDPOINTS
# ============================================

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "resume_loaded": screening_store["resume_text"] is not None,
        "job_loaded": screening_store["job_text"] is not None
    }

@app.post("/upload/resume", response_model=UploadResponse)
async def upload_resume(file: UploadFile = File(...)):
    """Upload resume PDF or TXT"""
    content = await file.read()

    if file.filename.endswith('.pdf'):
        text = extract_text_from_pdf(content)
    elif file.filename.endswith('.txt'):
        text = extract_text_from_txt(content)
    else:
        raise HTTPException(
            status_code=400,
            detail="Only PDF or TXT files supported!"
        )

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from file!"
        )

    screening_store["resume_text"] = text
    screening_store["resume_filename"] = file.filename

    return UploadResponse(
        message="Resume uploaded successfully!",
        filename=file.filename,
        text_length=len(text)
    )

@app.post("/upload/job", response_model=UploadResponse)
async def upload_job(file: UploadFile = File(...)):
    """Upload job description PDF or TXT"""
    content = await file.read()

    if file.filename.endswith('.pdf'):
        text = extract_text_from_pdf(content)
    elif file.filename.endswith('.txt'):
        text = extract_text_from_txt(content)
    else:
        raise HTTPException(
            status_code=400,
            detail="Only PDF or TXT files supported!"
        )

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from file!"
        )

    screening_store["job_text"] = text
    screening_store["job_filename"] = file.filename

    return UploadResponse(
        message="Job description uploaded successfully!",
        filename=file.filename,
        text_length=len(text)
    )

@app.post("/screen", response_model=ScreeningResponse)
def screen_resume():
    """Screen resume against job description"""

    if not screening_store["resume_text"]:
        raise HTTPException(
            status_code=400,
            detail="Please upload resume first!"
        )

    if not screening_store["job_text"]:
        raise HTTPException(
            status_code=400,
            detail="Please upload job description first!"
        )

    start = time.time()

    try:
        # Analyze resume
        print("Analyzing resume...")
        analysis = analyze_resume_and_job(
            screening_store["resume_text"],
            screening_store["job_text"]
        )

        # Get detailed suggestions
        print("Generating suggestions...")
        suggestions = get_improvement_suggestions(
            screening_store["resume_text"],
            screening_store["job_text"],
            analysis
        )

        time_taken = round(time.time() - start, 2)

        return ScreeningResponse(
            match_score=analysis.get("match_score", 0),
            summary=analysis.get("summary", ""),
            matching_skills=analysis.get("matching_skills", []),
            missing_skills=analysis.get("missing_skills", []),
            strengths=analysis.get("strengths", []),
            improvements=analysis.get("improvements", []),
            experience_match=analysis.get("experience_match", ""),
            recommendation=analysis.get("recommendation", ""),
            detailed_suggestions=suggestions,
            time_taken=time_taken
        )

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="AI response parsing failed. Please try again."
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Screening failed: {str(e)}"
        )

@app.delete("/clear")
def clear_data():
    """Clear uploaded files"""
    screening_store["resume_text"] = None
    screening_store["job_text"] = None
    screening_store["resume_filename"] = None
    screening_store["job_filename"] = None
    return {"message": "Data cleared successfully!"}

@app.get("/status")
def get_status():
    """Get current upload status"""
    return {
        "resume": screening_store["resume_filename"],
        "job": screening_store["job_filename"],
        "ready_to_screen": (
            screening_store["resume_text"] is not None and
            screening_store["job_text"] is not None
        )
    }