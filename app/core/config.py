from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    bot_token: str
    telegram_bot_link: str

    ollama_url: str
    ollama_model: str

    database_url: str
    
    class Config:
        env_file = ".env"


settings = Settings()