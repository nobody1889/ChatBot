from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.services.telegram import polling
from app.db import init_db
from app.api import router
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    task = None
    try:
        await init_db() # init database
        task = asyncio.create_task(polling())   # strat the telegram pooling
        yield

    finally:
        await task.cancel()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {
        "message": {
            "text":"wellcome to chatbot",
            "bot": "https://t.me/my_chatbot_ai_botss"
            }
        }

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)