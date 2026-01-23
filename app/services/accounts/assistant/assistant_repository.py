from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.assistant import AssistantCreate, AssistantDelete, AssistantRead
from app.models.assistant import Assistant
from sqlalchemy import select
from typing import List, Optional

class AssistantRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, assisstant: AssistantCreate)-> Assistant:
        assisstant_db = Assistant(**assisstant.model_dump())
        self.db.add(assisstant_db)

        await self.db.flush()
        return assisstant_db

    async def get_by_user_id(self, user_id: int)-> List:
        query = select(Assistant).where(Assistant.user_id == user_id)
        result = await self.db.execute(query)
        return result.scalars().all()
        

    async def get_by_name(self, user_id: int, name: str) -> Optional[Assistant]:
        query = select(Assistant).where(Assistant.user_id == user_id)
        query = query.where(Assistant.name == name)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    
    async def delete(self, assistant: AssistantDelete)-> bool:
        query = select(Assistant).where(Assistant.user_id == assistant.user_id)
        
        if assistant.name:
            query = query.where(Assistant.name == assistant.name)
        else:
            query = query.where(Assistant.id == assistant.id)
        
        result = await self.db.execute(query)
        
        assistant_obj = result.scalar_one_or_none()

        if assistant_obj:
            await self.db.delete(assistant_obj)
            await self.db.flush()
            return True

        return False