import json
import httpx
from app.core import settings

class BotClient:
    def __init__(self):
        self.base_url = f"https://api.telegram.org/bot{settings.bot_token}"
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=httpx.Timeout(15.0),
        )

    async def close(self):
        
        await self._client.aclose()

    async def sendMessage(self, chat_id: int, text: str, reply_message_id: int | None = None, reply_markup: dict | None = None, switch_inline_query_current_chat: str | None = None):
        payload = {
            "chat_id": chat_id,
            "text": text,
        }

        if reply_markup:
            payload["reply_markup"] = json.dumps(reply_markup)
        if reply_message_id:
            payload["reply_parameters"] = json.dumps({
                "message_id": reply_message_id,
                })
        if switch_inline_query_current_chat:
            payload["switch_inline_query_current_chat"] = switch_inline_query_current_chat

        r = await self._client.post(
            "/sendMessage",
            data=payload,
        )
        r.raise_for_status()
        return r.json()

    async def getUpdates(self, offset: int = 0, timeout: int = 10) -> dict:
        r = await self._client.get(
            "/getUpdates",
            params={
                "offset": offset,
                "timeout": timeout,
            },
        )
        r.raise_for_status()
        return r.json()
