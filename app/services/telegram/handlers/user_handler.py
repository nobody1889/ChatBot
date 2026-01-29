from ..bot_client import BotClient
from app.schemas import UserCreate, UserRead
import httpx

class UserHandler:
    def __init__(self, bot: BotClient):
        self.base_url = f"http://v1/accounts/"
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=httpx.Timeout(15.0),
        )

        self.bot = bot

    async def get_or_create_user(self, data: dict) -> UserRead:
        user_create = UserCreate(
            user_id=data["chat"]["id"],
            username=data["from"].get("username"),
            first_name=data["from"].get("first_name"),
            last_name=data["from"].get("last_name"),
        ) 

        r = await self.bot._client.get(
            f"/user/{user_create.user_id}",
        )

        if r.status_code == 200:
            user = r.json()
        else:
            user = await self._client.post(
                "/user",
                json=user_create,
            )
            user = r.json()

        return user