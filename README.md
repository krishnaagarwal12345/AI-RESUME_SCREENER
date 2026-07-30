# 🤖 AI Resume Screener

## Overview
An AI-powered resume screening system that analyzes
resumes against job descriptions and provides instant
match scores, skill analysis and career suggestions.

## ✨ Features
✅ Upload resume PDF or TXT
✅ Upload job description PDF or TXT
✅ AI-powered skill matching
✅ Match score with animated visualization
✅ Missing skills identification
✅ Personalized career suggestions
✅ Beautiful dark theme UI
✅ Dockerized for easy deployment

## 🛠️ Tech Stack
- **Backend**: Python + FastAPI
- **AI**: Groq API + Llama 3.3 70B
- **PDF Processing**: PyMuPDF
- **Frontend**: HTML + CSS + JavaScript
- **Deployment**: Docker + Docker Compose

## 🚀 How to Run

### Option 1 — Docker (Recommended)
```bash
# Clone repository
git clone https://github.com/krishnaagarwal12345/ai-resume-screener

# Create .env file
echo "GROQ_API_KEY=your_key_here" > .env

# Run with Docker Compose
docker-compose up

# Open browser
# http://localhost:8002
```

### Option 2 — Local
```bash
pip install -r requirements.txt
python -m uvicorn app:app --reload --port 8002
```

## 📊 How It Works
Upload Resume + Job Description
↓
PyMuPDF extracts text
↓
Groq API sends to Llama AI
↓
AI analyzes and returns JSON
↓
Match score + skill analysis displayed

## 🔌 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Frontend UI |
| GET | /health | Health check |
| POST | /upload/resume | Upload resume |
| POST | /upload/job | Upload job description |
| POST | /screen | Screen resume |
| DELETE | /clear | Clear data |
| GET | /status | Upload status |

## 👨‍💻 Created By
Krishna Agarwal — Final Year CS Student
AI/ML Developer | Java + Python + GenAI
