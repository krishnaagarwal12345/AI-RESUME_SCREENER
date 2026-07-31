# 🚀 AI Resume Screener

### AI-Powered Resume Screening & ATS Analysis Platform

Analyze resumes against job descriptions using **Groq AI** and **Llama 3.3 70B** to generate intelligent ATS compatibility scores, identify missing skills, and receive personalized career recommendations.

---

### ⭐ Key Highlights

- 🤖 AI-Powered Resume Screening
- 📊 ATS Compatibility Score
- 🎯 Skill Matching Analysis
- 🚫 Missing Skills Detection
- 💡 Personalized Career Suggestions
- 📄 PDF & TXT Resume Support
- ⚡ FastAPI Backend
- 🐳 Docker Ready
- 🌙 Modern Dark UI
- 🔥 Powered by Groq AI + Llama 3.3 70B

---

# 📖 About The Project

Recruiters often spend only a few seconds reviewing each resume. This project automates the initial screening process using Large Language Models (LLMs).

The application compares a candidate's resume against a job description, analyzes the required skills, identifies missing competencies, calculates an ATS compatibility score, and provides AI-generated career recommendations.

This project demonstrates how Generative AI can be integrated with FastAPI to build intelligent HR automation tools suitable for learning, experimentation, and portfolio development.

---

# ✨ Features

✅ Upload Resume (PDF / TXT)

✅ Upload Job Description (PDF / TXT)

✅ AI-Powered Resume Analysis

✅ ATS Compatibility Score

✅ Skill Matching

✅ Missing Skills Detection

✅ Career Recommendations

✅ Responsive Dark Theme UI

✅ REST API Architecture

✅ FastAPI Backend

✅ Docker Deployment

✅ Environment Variable Configuration

✅ JSON-Based AI Responses

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Backend | FastAPI |
| Programming Language | Python |
| AI Provider | Groq API |
| AI Model | Llama 3.3 70B |
| PDF Processing | PyMuPDF |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Docker, Docker Compose |
| Version Control | Git & GitHub |

---

# 🔄 Project Workflow

The application follows a simple and efficient AI-powered workflow:

```text
Resume (PDF/TXT)
        │
        ▼
Job Description (PDF/TXT)
        │
        ▼
Text Extraction using PyMuPDF
        │
        ▼
Prompt Generation
        │
        ▼
Groq API
        │
        ▼
Llama 3.3 70B
        │
        ▼
AI Analysis
        │
        ▼
JSON Response
        │
        ▼
ATS Score
Matched Skills
Missing Skills
Career Suggestions
        │
        ▼
Results Displayed on Dashboard
```

This workflow enables fast, AI-powered resume evaluation and provides meaningful insights to help candidates understand how well their resumes align with a specific job description.

---

# 🏗️ System Architecture

```text
                +-----------------------+
                |     Web Browser       |
                +-----------+-----------+
                            |
                            |
                     HTML + CSS + JS
                            |
                            ▼
                  FastAPI Application
                            |
            +---------------+---------------+
            |                               |
            |                               |
      Resume Parser                  Job Description
      (PyMuPDF)                      Text Processing
            |                               |
            +---------------+---------------+
                            |
                            ▼
                     Prompt Generator
                            |
                            ▼
                    Groq API Request
                            |
                            ▼
                    Llama 3.3 70B Model
                            |
                            ▼
                     JSON AI Response
                            |
                            ▼
                  Resume Analysis Results
```

# 📂 Project Structure

```text
AI-RESUME_SCREENER/
│
├── static/
│   └── index.html
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .dockerignore
├── .env.example
└── LICENSE
```

### Folder Description

| File / Folder | Description |
|--------------|-------------|
| **app.py** | Main FastAPI application containing API routes, AI integration and business logic |
| **static/** | Frontend files (HTML, CSS, JavaScript) |
| **Dockerfile** | Docker image configuration |
| **docker-compose.yml** | Multi-container deployment configuration |
| **requirements.txt** | Python dependencies |
| **README.md** | Project documentation |
| **.env.example** | Sample environment variables |
| **LICENSE** | Project license |

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/krishnaagarwal12345/AI-RESUME_SCREENER.git

cd AI-RESUME_SCREENER
```

---

## Create Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
uvicorn app:app --reload --port 8002
```

Open your browser:

```
http://localhost:8002
```

---

# 🐳 Docker Deployment

Build and start the application using Docker Compose.

```bash
docker-compose up --build
```

Visit:

```
http://localhost:8002
```

To stop the containers:

```bash
docker-compose down
```

Docker ensures a consistent environment and simplifies deployment across different systems.

---

# 🔐 Environment Variables

Before running the application, create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

> **Important**
>
> - Never commit your `.env` file to GitHub.
> - Use `.env.example` as a template for contributors.
> - Keep your API keys private.

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|:------:|----------|-------------|
| GET | `/` | Opens the frontend application |
| GET | `/health` | Health check endpoint |
| POST | `/upload/resume` | Upload a resume (PDF/TXT) |
| POST | `/upload/job` | Upload a job description (PDF/TXT) |
| POST | `/screen` | Analyze resume against job description |
| DELETE | `/clear` | Clear uploaded files |
| GET | `/status` | Check upload status |

---

# 💼 Why This Project?

Recruiters often review hundreds of resumes for a single job opening. Manually comparing resumes with job descriptions is time-consuming and inconsistent.

This project demonstrates how Generative AI can automate the initial screening process by:

- Comparing resumes with job descriptions
- Identifying matching and missing skills
- Calculating an ATS compatibility score
- Providing personalized career recommendations

It also serves as a practical example of integrating Large Language Models (LLMs) into a real-world web application using FastAPI.

---

# 🚀 Roadmap

### Completed

- [x] Resume Upload
- [x] Job Description Upload
- [x] PDF Parsing
- [x] Groq AI Integration
- [x] ATS Compatibility Score
- [x] Skill Matching
- [x] Missing Skills Detection
- [x] Career Suggestions
- [x] Docker Support

### Planned

- [ ] User Authentication
- [ ] Resume History
- [ ] PDF Report Download
- [ ] AI Cover Letter Generator
- [ ] AI Interview Question Generator
- [ ] Admin Dashboard
- [ ] Cloud Deployment
- [ ] Multi-language Support

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you would like to contribute:

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

Please ensure your code follows clean coding practices and includes appropriate documentation where necessary.

---

# 📄 License

This repository is licensed under the terms specified in the `LICENSE` file.

Please review the license before using, modifying, or redistributing this project.

---

# 👨‍💻 Author

## Krishna Agarwal

Final Year Computer Science Engineering Student

**Interests**

- Artificial Intelligence
- Generative AI
- FastAPI
- Python
- Java
- Full Stack Development

Feel free to connect for collaboration, feedback, or project discussions.

---

# ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork the project
- 🐞 Report bugs
- 💡 Suggest new features
- 📢 Share it with others

Your support helps improve the project and motivates future development.

---

# 🙏 Acknowledgements

This project makes use of several outstanding open-source technologies and services:

- FastAPI
- Groq API
- Llama 3.3
- PyMuPDF
- Docker
- HTML, CSS, and JavaScript

Special thanks to the open-source community for creating tools that make AI application development more accessible.

---

