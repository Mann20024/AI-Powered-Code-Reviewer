import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# Import your reviewer logic
from app.review.ai_reviewer import ai_review

# Define Request Schema
class CodeRequest(BaseModel):
    code: str
    language: str

app = FastAPI()

# FIX: Point to app/templates
# __file__ is app/main.py, so dirname(__file__) is the 'app' folder
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(CURRENT_DIR, "templates")
templates = Jinja2Templates(directory=template_path)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/review")
async def review_code(request: CodeRequest):
    # This calls the parser-enabled ai_review
    result = ai_review(request.code, request.language)
    return result