import os
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from app.core.config import settings
class RAGService:
    def __init__(self):
        self.embeddings = FastEmbedEmbeddings()
        self.llm = self._initialize_llm()
        self.vector_store = self._initialize_vector_store()
        self.qa_chain = self._build_chain()

    def _initialize_llm(self):
        return ChatOpenAI(
            api_key = settings.openrouter_api_key,
            base_url=settings.openrouter_api_base,
            model = settings.model_name,
            temperature=settings.temperature
        )
    
    def _initialize_vector_store(self):
        if not os.path.exists(settings.data_path):
            raise FileNotFoundError(f"Nie znaleziono pliku bazy wiedzy: {settings.data_path}")

        loader = TextLoader(settings.data_path, encoding="utf-8")
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(docs)

        return FAISS.from_documents(chunks, self.embeddings)

    def _build_chain(self):
        retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})

        system_prompt = (
            "Jesteś asystentem AI. Odpowiedz na pytanie użytkownika "
            "korzystając WYŁĄCZNIE z poniższego kontekstu. Jeśli odpowiedź nie "
            "znajduje się w kontekście, powiedz, że nie wiesz.\n\n"
            "Kontekst:\n{context}"
        )
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])

        question_answer_chain = create_stuff_documents_chain(self.llm, prompt)

        return create_retrieval_chain(retriever, question_answer_chain)

    def ask_question(self, question: str) -> str:
        response = self.qa_chain.invoke({"input": question})
        return response["answer"]