from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from user_repository import UserRepository
from user_service import UserService
from app.core.logging import logging

logger = logging.getLogger(__name__)

def get_user_service(db: AsyncSession = Depends(get_db)):
    service = UserService(UserRepository(db))
    try:
        logger.info("User service initialized")
        yield service
    finally:
        logger.info("User service closed")
