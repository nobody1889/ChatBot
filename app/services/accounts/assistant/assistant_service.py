from .assistant_repository import AssistantRepository
from app.schemas.assistant import AssistantCreate, AssistantDelete

class AssistantService:
    def __init__(self, assistant_repo: AssistantRepository):
        self.assistant_repo = assistant_repo

    async def create_assistant(self, assistant: AssistantCreate):
        return self.assistant_repo.create(assistant)
    
    async def get_user_assistants(self, user_id: int):
        return await self.assistant_repo.get_by_user_id(user_id)

    async def get_user_assistant(self, user_id: int, name: str):
        return await self.assistant_repo.get_by_name(user_id, name)
    
    async def delete(self, assistant: AssistantDelete):
        return await self.assistant_repo.delete(assistant)