from fastapi import Depends
from fastapi.exceptions import FastAPIError
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from .user_repository import UserRepository
from .user_service import UserService
from app.core.logging import logging

logger = logging.getLogger(__name__)


async def get_user_service(db: AsyncSession = Depends(get_db)):
    service = UserService(UserRepository(db))
    try:
        logger.info("User service initialized")
        yield service
    
    except FastAPIError as e:
        logger.error(f"FastAPIError: {e}")
        raise e

    except Exception as e:
        logger.error(f"error in get_user_service: {e}")
        raise e
    
    finally:
        await db.commit()
        logger.info("User service closed")