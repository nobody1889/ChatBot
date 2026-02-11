from app.services.telegram.handlers.bot_client import BotClient
from app.core import settings
from app.services.telegram.handlers.gateways import AssistantHandler
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
            "switch_inline_query_current_chat": ""
        })

    return result

async def load_my_assistants(offset: int) -> list[dict]:
    assistants = await AssistantHandler().get_user_assistants(user_id=offset)
    result = []

    for assistant in assistants:
        result.append({
            "type": "article",
            "id": str(uuid.uuid4()),
            "title": assistant["name"],
            "description": assistant["name"],
            "input_message_content": {
                    "message_text": "/select_assistant " + assistant["name"],
                },
        })
    if not result:
        result.append({
            "type": "article",
            "id": str(uuid.uuid4()),
            "title": "No Assistants Found",
            "description": "No Assistants Found",
            "switch_inline_query_current_chat": ""
        })

    return result

async def load_users(offset: int) -> list[dict]:
    pass

async def load_my_users(offset: int) -> list[dict]:
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

LOADERS = {
    "new_assistant": lambda offset, q: load_assistants(query=q.split(":")[-1].strip(), offset=offset),
    "assistants_list": lambda offset, q: load_my_assistants(offset=offset),
    "new_user": lambda offset, q: load_users(offset),
    "users_list": lambda offset, q: load_my_users(offset),
}

async def handle_inline_query(bot: BotClient, inline_query: dict) -> None:
    query: str = inline_query["query"]
    offset = int(inline_query.get("offset") or 1)

    for prefix, loader in LOADERS.items():
        if query.startswith(prefix):
            result = await loader(offset, query)
            break
    else:
        result = await load_unknown()  
    
    await bot.answer_inline_query(inline_query["id"], result, next_offset=str(offset + 1))