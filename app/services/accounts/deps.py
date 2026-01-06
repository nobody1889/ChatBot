from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from user_repository import UserRepository
from user_service import UserService


def get_user_service(db: AsyncSession = Depends(get_db)):
    service = UserService(UserRepository(db))
    yield service
