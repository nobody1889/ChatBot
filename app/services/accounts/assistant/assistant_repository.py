from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.assistant import AssistantCreate, AssistantDelete, AssistantRead
from app.models.assistant import Assistant
from sqlalchemy import select, update
from typing import List, Optional
from sqlalchemy.sql import func

class AssistantRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, assisstant: Assistant)-> Assistant:
        self.db.add(assisstant)

        await self.db.flush()
        return assisstant

    async def get_by_user_id(self, user_id: int) -> List:
        query = select(Assistant).where(Assistant.user_id == user_id).order_by(Assistant.last_used_at.desc())
        result = await self.db.execute(query)
        return result.scalars().all()
        

    async def get_by_model(self, user_id: int, model: str) -> Optional[Assistant]:
        query = select(Assistant).where(Assistant.user_id == user_id).order_by(Assistant.last_used_at.desc())
        query = query.where(Assistant.model == model)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def set_assistant_default(self, user_id: int, model: str) -> List:
        query = (
        update(Assistant)
        .where(Assistant.user_id == user_id)
        .where(Assistant.model == model)
        .values(last_used_at=func.now())
        )

        await self.db.execute(query)
        await self.db.flush()

        return await self.get_by_user_id(user_id)

    async def delete(self, data: AssistantDelete)-> bool:
        query = select(Assistant).where(Assistant.user_id == data.user_id)
        
        if data.model:
            query = query.where(Assistant.model == data.model)
        else:
            query = query.where(Assistant.id == data.id)
        
        result = await self.db.execute(query)
        
        assistant_obj = result.scalar_one_or_none()

        if assistant_obj:
            await self.db.delete(assistant_obj)
            await self.db.flush()
            return True

        return False