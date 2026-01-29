from ..bot_client import BotClient
from app.schemas import UserCreate
import httpx

class UserHandler:
    def __init__(self, bot: BotClient):
        self.base_url = "http://localhost:8000/api/v1/accounts"
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=httpx.Timeout(15.0),
        )

        self.bot = bot

    async def get_or_create_user(self, data: dict) -> dict:
        user_create = UserCreate(
            user_id=str(data["from"]["id"]),
            username=data["from"].get("username"),
            first_name=data["from"].get("first_name"),
            last_name=data["from"].get("last_name"),
        ) 

        resp = await self._client.get(
            f"/user/{user_create.user_id}",
        )

        if resp.status_code == 200:
            user = resp.json()
        else:
            resp = await self._client.post(
                "/user",
                json=user_create.model_dump(),
            )
            user = resp.json()

        return user
    
    async def close(self):
        await self._client.aclose()