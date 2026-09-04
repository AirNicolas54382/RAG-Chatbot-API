from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Pydantic wymusi obecność tego klucza w .env - jeśli go nie będzie, apka się nie uruchomi (fail-fast)
    openrouter_api_key: str
    openrouter_api_base: str = "https://openrouter.ai/api/v1"
    
    # Parametry modelu
    model_name: str = "openrouter/free"
    temperature: float = 0.7
    
    # Model do zamiany tekstu na wektory (darmowy, uruchamia się lokalnie)
    embeddings_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    
    # Ścieżka do bazy wiedzy
    data_path: str = "data/text.txt"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# Instancja konfiguracyjna używana w reszcie aplikacji
settings = Settings()