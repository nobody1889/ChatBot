from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    bot_token: str
    ollama_url: str
    ollama_model: str
    
    class Config:
        env_file = ".env"


settings = Settings()