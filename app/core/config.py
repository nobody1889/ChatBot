from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    port: int
    
    bot_token: str
    telegram_bot_link: str

    ollama_url: str
    ollama_models: List[str]

    database_url: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()