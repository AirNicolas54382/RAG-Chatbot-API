from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openrouter_api_key: str
    openrouter_api_base: str = "https://openrouter.ai/api/v1"

    model_name: str = "openrouter/free"
    temperature: float = 0.7
    
    embeddings_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    
    data_path: str = "data/text.txt"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()