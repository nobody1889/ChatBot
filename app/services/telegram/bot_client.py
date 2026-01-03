import httpx
from app.core import settings

class BotClient:
    def __init__(self):
        self.base_url = f"https://api.telegram.org/bot{settings.bot_token}"
        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=httpx.Timeout(15.0),
        )

    async def close(self):
        await self.client.aclose()

    async def sendMessage(self, chat_id: str, text: str) -> dict:
        r = await self.client.post(
            "/sendMessage",
            params={
                "chat_id": chat_id,
                "text": text,
            },
        )
        r.raise_for_status()
        return r.json()

    async def getUpdates(self, offset: int = 0, timeout: int = 10) -> dict:
        r = await self.client.get(
            "/getUpdates",
            params={
                "offset": offset,
                "timeout": timeout,
            },
        )
        r.raise_for_status()
        return r.json()
