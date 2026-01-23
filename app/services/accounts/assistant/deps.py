from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from .assistant_service import AssistantService
from app.core.logging import logging

logger = logging.getLogger(__name__)

async def get_assistant_service(db: AsyncSession = Depends(get_db)):
    service = AssistantService((db))
    try:
        logger.info("Assistant service initialized")
        yield service
    finally:
        await db.commit()
        logger.info("Assistant service closed")