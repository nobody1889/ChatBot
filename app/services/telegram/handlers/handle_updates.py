from .handle_commands import command_handler
from .handle_ai import handle_ai_message
from .user_handler import UserHandler
from .handle_callback_query import handle_callback_query

async def handle_user(bot, data: dict) -> dict | None:
    chat_id = str(data["chat"]["id"])

    handler = UserHandler(bot=bot)
    user: dict = await handler.get_or_create_user(data = data)

    if user.get("is_blocked"):
        await bot.sendMessage(chat_id, "🚫 You are blocked.")
        return
    
    return user
    
async def handle_message(bot, message: dict) -> None:
    user = await handle_user(bot, message)
    if not user:
        return

    text: str | None = message.get("text")
    chat_id: str = str(message["chat"]["id"])

    if text:
        if text.startswith("/"):
            await command_handler(bot, chat_id, text)
        else:
            await handle_ai_message(bot, chat_id, text)
    else:
        await bot.sendMessage(chat_id, "i just handle text message 💔💔")
    
async def dispatcher(bot, update: dict):
    match update:
        case {"callback_query": callback_query}:
            await handle_callback_query(bot, callback_query)
        
        case {"message": message}:
            await handle_message(bot, message)

        case _:
            return
    
    

    
