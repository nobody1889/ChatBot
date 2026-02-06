from ..bot_client import BotClient
from app.core import settings

async def load_assistants(offset: int) -> list[dict]:
    models:list = settings.ollama_models
    result = []

    start = (offset-1) * 10
    end = offset * 10

    for model in models[start:end]:
        result.append({
            "type": "article",
            "id": model,
            "title": model,
            "description": model,
            "input_message_content": {
                "message_text": model,
            },
        })

    return result

async def load_users(offset: int) -> list[dict]:
    pass

async def handle_inline_query(bot: BotClient, inline_query: dict) -> None:
    query: str = inline_query["query"]
    offset = int(inline_query.get("offset", 1))

    if "assistant" in query.split["_"]:
        result = await load_assistants(offset)
    if "user" in query.split["_"]:
        result = await load_users(offset)

    await bot.answer_inline_query(inline_query["id"], result)

    

async def handle_chosen_inline_result(bot: BotClient, chosen_inline_result: dict) -> None:
    print(f"Received chosen inline result: {chosen_inline_result}")