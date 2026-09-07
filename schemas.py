from pydantic import BaseModel
class QuestionRequest(BaseModel):
    question:str
class QuestionResponse(BaseModel):
    answar:str
    sources:list[str]