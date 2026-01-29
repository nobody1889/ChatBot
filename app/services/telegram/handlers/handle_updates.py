from .handle_commands import command_handler
from .handle_ai import handle_ai_message
from .user_handler import UserHandler
from app.schemas import UserRead

async def dispatcher(bot, update: dict):
    if "message" not in update:
        return
    
    handler = UserHandler(bot=bot)

    message: dict = update["message"]
    chat_id = str(message["chat"]["id"])
    text: str = message.get("text")

    
    user: UserRead = await handler.get_or_create_user(data = message)

    if user.is_blocked:
        await bot.sendMessage(chat_id, "🚫 You are blocked.")
        return

    if text:
        if text.startswith("/"):
            await command_handler(bot, chat_id, text)
        else:
            await handle_ai_message(bot, chat_id, text)
    else:
        await bot.sendMessage(chat_id, "i just handle text message 💔💔")
