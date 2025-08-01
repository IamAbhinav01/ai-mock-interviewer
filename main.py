from fastapi import FastAPI, Request, UploadFile, Form,status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
from llm_parser import extract_skills_from_resume
from llm_question_generator import generate_questions
from llm_feedback_generator import evaluate_answer

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


from collections import defaultdict
user_sessions = defaultdict(dict)

@app.get("/")
async def show_uploader(request: Request):
    return templates.TemplateResponse("file_uploader.html", {"request": request})

@app.post("/dashboard")
async def dashboard(request: Request, resume: UploadFile):
    text = await resume.read()
    decoded = text.decode("utf-8", errors="ignore")
    clean_text = decoded.strip().replace("\n", " ")
    if len(clean_text) > 5000:
        clean_text = clean_text[:5000]

    skills = extract_skills_from_resume(clean_text)
    return templates.TemplateResponse("dashboard.html", {"request": request, "skills": skills})

@app.get("/interview/{skill}", response_class=HTMLResponse)
async def start_interview(request: Request, skill: str):
    questions = generate_questions(skill)
    user_sessions[skill]["questions"] = questions
    user_sessions[skill]["answers"] = []
    return templates.TemplateResponse("interview.html", {
        "request": request,
        "skill": skill,
        "question": questions[0],
        "index": 0,
        "total": len(questions),
        "complete": False
    })

@app.get("/back-to-dashboard", response_class=RedirectResponse)
async def back_to_dashboard():
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/interview/{skill}", response_class=HTMLResponse)
async def handle_answer(request: Request, skill: str, index: int = Form(...), answer: str = Form(...)):
    questions = user_sessions[skill]["questions"]
    user_sessions[skill]["answers"].append(answer)

    # Get current question
    question = questions[index]
    
    # Call LLM to evaluate answer
    feedback = evaluate_answer(question, answer, skill)

    next_index = index + 1
    if next_index >= len(questions):
        return templates.TemplateResponse("interview.html", {
            "request": request,
            "skill": skill,
            "total": len(questions),
            "complete": True
        })

    return templates.TemplateResponse("interview.html", {
        "request": request,
        "skill": skill,
        "question": questions[next_index],
        "index": next_index,
        "total": len(questions),
        "complete": False,
        "feedback": feedback
    })
