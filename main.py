from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


# --------------------------------------------------
# Project directory
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent


# --------------------------------------------------
# FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)


# --------------------------------------------------
# Static files
# --------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


# --------------------------------------------------
# Templates
# --------------------------------------------------

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# --------------------------------------------------
# Request models
# --------------------------------------------------

class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=5000
    )


class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=20000
    )


# --------------------------------------------------
# Home page
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "EduGenie"
        }
    )


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "message": "EduGenie backend is running"
    }


# --------------------------------------------------
# Q&A
# --------------------------------------------------

@app.post("/qa")
async def qa(request: QuestionRequest):
    try:
        result = answer_question(request.question)
        return {"result": result}
    except Exception as e:
        print("QA ERROR:", repr(e))
        raise HTTPException(status_code=500, detail=str(e))


# --------------------------------------------------
# Explanation
# --------------------------------------------------

@app.post("/explain")
async def explain(request: TextRequest):

    try:

        result = explain_topic(
            request.text
        )

        return {
            "result": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# --------------------------------------------------
# Quiz
# --------------------------------------------------

@app.post("/quiz")
async def quiz(request: TextRequest):

    try:

        result = generate_quiz(
            request.text
        )

        return {
            "quiz": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# --------------------------------------------------
# Summarization
# --------------------------------------------------

@app.post("/summarize")
async def summarize(request: TextRequest):

    try:

        result = summarize_text(
            request.text
        )

        return {
            "result": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# --------------------------------------------------
# Learning recommendations
# --------------------------------------------------

@app.post("/learn/recommendations")
async def learning_recommendations(
    request: TextRequest
):

    try:

        result = get_learning_recommendations(
            request.text
        )

        return {
            "result": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )