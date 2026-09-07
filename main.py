from fastapi import FastAPI
from app.schemas import QuestionRequest,QuestionResponse
from app.rag import generate_answer
app=FastAPI(
    title="Gemini RAG API",
    description="RAG based Question Answering API",
    version="1.0.0"
)
@app.get("/")
def home():
    return {
        "message":"Gemini RAG API is running"
    }
@app.post("/ask",response_model=QuestionResponse)
def ask_question(request:QuestionRequest):
    result=generate_answer(request.question)
    return result

