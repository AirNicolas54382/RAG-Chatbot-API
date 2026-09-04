from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router

app = FastAPI(
    title="RAG Chatbot API",
    description="Profesjonalne API do rozmów z botem RAG przy użyciu LangChain i FAISS.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/", tags=["root"])
async def root():
    """
    Powitalny endpoint
    """
    return{
        "message": "API RAG Bota działa poprawnie.",
        "docs": "Przejdź pod /docs, aby przetestować endpointy w Swagger UI"
    }