from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.services.telegram import pooling 
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        task = asyncio.create_task(pooling())
        yield

    finally:
        task.cancel()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {
        "message": {
            "text":"wellcome to chatbot",
            "bot": "https://t.me/my_chatbot_ai_botss"
            }
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)