from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Json
from typing import List

class Settings(BaseSettings):
    bot_token: str
    telegram_bot_link: str

    ollama_url: str
    ollama_models: Json[List[str]]

    database_url: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()