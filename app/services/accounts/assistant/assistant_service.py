from .assistant_repository import AssistantRepository
from app.services.accounts.user.user_repository import UserRepository
from app.schemas.assistant import AssistantCreate, AssistantDelete
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.models.assistant import Assistant

class AssistantService:
    def __init__(self, db: AsyncSession):
        self.assistant_repo = AssistantRepository(db)
        self.user_repo = UserRepository(db)

    async def create_assistant(self, data: AssistantCreate):
        user = await self.user_repo.get_by_user_id(data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail=f"User {data.user_id} not found")
        assistant = Assistant(
            user_id=user.id,
            name=data.name,
            model=data.model
        )
        return await self.assistant_repo.create(assistant)
    
    async def get_user_assistants(self, telegram_user_id: str):
        user = await self.user_repo.get_by_user_id(telegram_user_id)
        if not user:
            raise HTTPException(status_code=404, detail=f"User {telegram_user_id} not found")
        return await self.assistant_repo.get_by_user_id(user.id)

    async def get_user_assistant(self, telegram_user_id: str, name: str):
        user = await self.user_repo.get_by_user_id(telegram_user_id)
        if not user:
            raise HTTPException(status_code=404, detail=f"User {telegram_user_id} not found")
        assistant = await self.assistant_repo.get_by_name(user.id, name)
        if not assistant:
            raise HTTPException(status_code=404, detail="Assistant not found")
        return assistant
    
    async def delete(self, data: AssistantDelete):
        user = await self.user_repo.get_by_user_id(data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail=f"User {data.user_id} not found")
        data.user_id = user.id
        success = await self.assistant_repo.delete(data)
        if not success:
            raise HTTPException(status_code=404, detail="Assistant not found")
        return True
