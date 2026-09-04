# RAG Chatbot API 🤖

A professional backend API built with **FastAPI** and **LangChain**, implementing the Retrieval-Augmented Generation (RAG) architecture. 

This project serves as an interface for chatting with an AI model that bases its responses exclusively on a provided, local knowledge base. The architecture was designed with modern standards, modularity, and testability in mind.

## 🚀 Technologies & Architecture

* **FastAPI:** A high-performance web framework with automatic documentation (Swagger UI) and Pydantic validation.
* **LangChain (LCEL):** AI logic built using the modern *LangChain Expression Language* standard, replacing deprecated legacy chains (e.g., `RetrievalQA`).
* **FastEmbed:** A lightweight and incredibly fast text vectorization library (Embeddings) based on ONNX Runtime. It bypasses heavy dependencies (like PyTorch) while maintaining high-quality results on CPU.
* **FAISS:** A local, in-memory vector store developed by Facebook AI.
* **OpenRouter / OpenAI:** Integration with external Large Language Models using the modern Chat Models standard.
* **Pydantic Settings:** Secure configuration management utilizing the "Fail-Fast" design pattern for API keys.

## 📁 Project Structure

The application uses a layered architecture (Routing, Services, Configuration), which makes the code easier to manage and scale:

```text
├── app/
│   ├── api/
│   │   └── routes.py         # FastAPI endpoints and routing
│   ├── core/
│   │   └── config.py         # Environment variables management (pydantic-settings)
│   ├── services/
│   │   └── rag_service.py    # AI business logic, LCEL, FAISS
│   └── main.py               # FastAPI initialization and CORS setup
├── data/
│   └── text.txt              # Sample knowledge base for the AI model
├── .env                      # (Ignored) API Keys
├── .gitignore
├── requirements.txt
└── README.md
