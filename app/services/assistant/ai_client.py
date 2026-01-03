import json
import httpx
from app.core import settings
from app.core import logging

logger = logging.getLogger(__name__)

class AiClient:
    def __init__(self):
        self.base_url = settings.ollama_url
        self.model = settings.ollama_model

        self.client = httpx.AsyncClient(
            headers={"Content-Type": "application/json"},
            base_url=self.base_url,
            timeout=60,
        )

    async def chat(self, message: str, temperature=0.7) -> str:
        """
        messages: list of {role: system|user, content: str}
        """

        messages = [
            { "role": "system", "content": "You are a helpful assistant." },
            {"role": "user","content": message},
        ]

        response = await self.client.post(
            "/api/chat",
            json={
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
            },
        )

        response.raise_for_status()

        final_text = ""
        for line in response.text.splitlines():
            data = json.loads(line)
            final_text += data.get("message", {}).get("content", "")

        return final_text

    async def generate(self, prompt: str, temperature=0.7, max_tokens=200):

        prompt = [
            { "role": "system", "content": "You are a helpful assistant." },
            {"role": "user","content": prompt},
        ]

        response = await self.client.post(
            "/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "temperature": temperature,
                "num_predict": max_tokens,
            },
        )
        response.raise_for_status()
        return response.json()["response"]

    async def stream_chat(self, message: str):

        messages = [
            { "role": "system", "content": "You are a helpful assistant." },
            {"role": "user","content": message},
        ]

        async with self.client.stream(
            "POST",
            "/api/chat",
            json={
                "model": self.model,
                "messages": messages,
                "stream": True,
            },
        ) as response:
            response.raise_for_status()

            async for line in response.aiter_lines():
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    if "message" in data:
                        yield data["message"]["content"]
                except json.JSONDecodeError:
                    logger.error("invalid json data", line)

    async def close(self):
        await self.client.aclose()


