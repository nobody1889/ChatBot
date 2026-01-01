import httpx
from app.core import settings

class BotClient:
    def __init__(self):
        self.base_url = f"https://api.telegram.org/bot{settings.bot_token}"
        self.client = httpx.Client(base_url=self.base_url)

    async def close(self):
        await self.client.aclose()

    async def sendMessage(self, chat_id: str, text: str) -> dict:
        return await self.client.post(
            "/sendMessage",
            params=
            {
                "chat_id": chat_id,
                "text": text,
            }
        )

    async def getUpdates(self, offset=0, limit=100) -> tuple:
        return await self.client.get(
            "/getUpdates",
            params=
            {
                "offset": offset,
            }
        ), offset