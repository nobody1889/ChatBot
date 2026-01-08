from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.services.telegram import polling
from app.db import init_db
from app.core import logging
from app.api import all_routes
import asyncio
import httpx

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await init_db() # init database
        logger.info("Database initialized successfully")

        task = asyncio.create_task(polling())   # strat the telegram poling

        yield

    finally:
        try:
            task.cancel()
            await task
            
        except asyncio.CancelledError:
            logger.info("Task cancelled")

        except UnboundLocalError:
            logger.error("task not found")
          
        except UnboundLocalError:
            logger.error("task not found")
        
        except httpx.ConnectError as e:
            logger.error(f"httpx.ConnectError: {e}")

        except Exception as e:
            logger.error(f"Error during shutdown: {e}", exc_info=True)
            

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {
        "message": {
            "text":"wellcome to chatbot",
            "bot": "https://t.me/my_chatbot_ai_botss"
            }
        }

app.include_router(all_routes)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)