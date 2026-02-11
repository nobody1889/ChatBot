from app.schemas import UserCreate
from app.core import settings
import httpx

class UserHandler:
    def __init__(self):
        self.base_url = f"http://localhost:{settings.port}/api/v1/accounts/"
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=httpx.Timeout(15.0),
        )

    async def get_or_create_user(self, data: dict) -> dict | None:
        user_create = UserCreate(
            user_id=str(data["from"]["id"]),
            username=data["from"].get("username"),
            first_name=data["from"].get("first_name"),
            last_name=data["from"].get("last_name"),
        ) 

        resp = await self._client.get(
            f"user/{user_create.user_id}",
        )

        if resp.status_code == 200:
            user = resp.json()
        else:
            resp = await self._client.post(
                "user/",
                json=user_create.model_dump(),
            )

            if resp.status_code != 200:
                return
            
            user = resp.json()
    
        return user

    async def close(self):
        await self._client.aclose()

class AssistantHandler:
    def __init__(self):
        self.base_url = f"http://localhost:{settings.port}/api/v1/assistant/"
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=httpx.Timeout(15.0),
        )
    
    async def set_or_add_assistant(self, user_id: str, assistant_name: str) -> dict | None:
        resp = await self._client.get( # check if assistant exists
            f"user/{user_id}/model/{assistant_name}",
        )

        if resp.status_code == 200: # set default assistant
            resp = await self._client.put(
                f"user/{user_id}/model/{assistant_name}",
            )
            return resp.json()
        
        elif resp.status_code == 404:
            resp = await self._client.post(
                json={
                    "model": assistant_name,
                    "user_id": user_id
                    },
            )

            if resp.status_code == 200:
                return resp.json()
        return
    
    async def get_user_assistants(self, user_id: str) -> list[dict] | None:
        resp = await self._client.get(
            f"user/{user_id}",
        )

        if resp.status_code == 200:
            return resp.json()
        else:
            return

    async def close(self):
        await self._client.aclose()