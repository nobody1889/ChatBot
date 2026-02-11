from app.services.telegram.handlers.bot_client import BotClient
from app.core import settings
import uuid

async def load_assistants(query: str, offset: int) -> list[dict]:
    models:list[str] = settings.ollama_models
    result = []

    start = (offset-1) * 10
    end = offset * 10

    for model in models[start:end]:
        if model.startswith(query):
            result.append({
                "type": "article",
                "id": str(uuid.uuid4()),
                "title": model,
                "description": model,
                "input_message_content": {
                    "message_text": "/select_assistant " + model,
                },
            })
    if not result:
        result.append({
            "type": "article",
            "id": str(uuid.uuid4()),
            "title": "Not Found",
            "description": "Not Found",
            "input_message_content": {
                    "message_text": "Not Found",
                },
        })

    return result

async def load_users(offset: int) -> list[dict]:
    pass

async def load_unknown() -> list[dict]:
    return [{
        "type": "article",
        "id": str(uuid.uuid4()),
        "title": "Unknown",
        "description": "Unknown",
        "input_message_content": {
                "message_text": "Unknown",
            },
    }]

async def handle_inline_query(bot: BotClient, inline_query: dict) -> None:
    query: str = inline_query["query"]
    offset = int(inline_query.get("offset") or 1)

    if "assistants" in query.split("_"):
        result = await load_assistants(query=query.split(": ")[-1], offset=offset)
    elif "users" in query.split("_"):
        result = await load_users(offset)
    else:
        result = await load_unknown()
    
    await bot.answer_inline_query(inline_query["id"], result)