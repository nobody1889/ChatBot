from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    bot_token: str = Field(..., env="BOT_TOEKN")    
    
    class Config:
        env_file = ".env"


settings = Settings()