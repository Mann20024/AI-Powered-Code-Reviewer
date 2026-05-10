from pydantic import BaseModel
from typing import List

class CodeRequest(BaseModel):
    code: str
    language: str

class ReviewResponse(BaseModel):
    score: str
    points: List[str]
    improved_code: str