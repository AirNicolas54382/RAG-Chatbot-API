from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Annotated

from app.services.rag_service import RAGService

router = APIRouter(prefix="/api/v1", tags=["chats"])

class ChatRequest(BaseModel):
    question: str

    class Config:
        json_schema_extra = {
            "example": {
                "question": "O czym jest ta aplikacja?"
            }
        }
class ChatResponse(BaseModel):
    answer: str

_rag_service_instance = None

def get_rag_service() -> RAGService:
    global _rag_service_instance
    if _rag_service_instance is None:
        try:
             _rag_service_instance = RAGService()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Błąd inicjalizacji serwisu AI: {str(e)}")
    return _rag_service_instance

RagServiceDep = Annotated[RAGService, Depends(get_rag_service)]


@router.post("/chat", response_model=ChatResponse)
async def chat_with_bot(request: ChatRequest, rag_service: RagServiceDep):
    try:
        answer = rag_service.ask_question(request.question)
        return ChatResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Błąd podczas generowania odpowiedzi: {str(e)}")

@router.get("/health")
async def health_check():
    return {"status": "ok", "message": "Bot RAG dziala"}