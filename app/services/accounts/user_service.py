from typing import Optional
from .user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def get_by_user_id(self, user_id: str) -> Optional[User]:
        return await self.user_repository.get_by_user_id(user_id)

    async def get_by_username(self, username: str) -> Optional[User]:
        return await self.user_repository.get_by_username(username)

    async def update_or_create(self, user: UserCreate) -> User:
        return await self.user_repository.update_or_create(user)
    
    async def get_or_create_user(self, user: UserCreate) -> User:
        return await self.user_repository.get_or_create(user)

    async def update_user(self, data: UserUpdate) -> User:
        user = await self.get_by_user_id(data.user_id)

        if hasattr(user, "is_blocked") and user.is_blocked:
            raise ValueError("Cannot update blocked status directly via update_user")
        
        return await self.user_repository.update(user=user, data=data)

    async def block_user(self, user_id: str) -> bool:
        return await self.user_repository.set_block(user_id, True)

    async def unblock_user(self, user_id: str) -> bool:
        return await self.user_repository.set_block(user_id, False)

    async def check_user_permitions(self, user_id: str) -> User:
        user = await self.user_repository.get_by_user_id(user_id)

        if not user:
            raise ValueError("User not found")
        
        if user.is_blocked:
            raise PermissionError("User is blocked")
        
        return user

    async def get_all_users(self) -> list[User]:
        return await self.user_repository.get_all_users()
    
    async def delete_user(self, user_id: str) -> bool:    
        return await self.user_repository.delete_user(user_id)