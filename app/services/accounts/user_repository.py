from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserUpdate
from typing import Optional
from sqlalchemy import select, update

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_user_id(self, user_id: str) -> Optional[User]:
        result = await self.db.execute(select(User).where(User.user_id == user_id))
        return result.scalar_one_or_none()

    async def get_by_username(self, username: str) -> Optional[User]:
        result = await self.db.execute(select(User).where(User.username == username))
        return result.scalar_one_or_none()

    async def create(self, user: UserCreate) -> User:
        user_db = User(**user.model_dump())
        self.db.add(user_db)
        
        await self.db.flush()
        return user_db

    async def update(self, user: User, data: UserUpdate) -> User:
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(user, key, value)
        await self.db.flush()
        return user

    async def set_block(self, user_id: str, block: bool) -> bool:
        result = await self.db.execute(
            update(User).where(User.user_id == user_id).values(is_blocked=block)
        )
        await self.db.flush()
        return result.rowcount > 0
