from .handle_commands import command_handler
from .handle_ai import handle_ai_message
from app.services.accounts import UserService


async def dispatcher(bot, update, user_service: UserService):
    if "message" not in update:
        return
    
    message: dict = update["message"]
    chat_id = str(message["chat"]["id"])
    text: str = message.get("text")

    user = await user_service.get_or_create_user(
        user_id=chat_id,
        username=message["from"].get("username"),
        first_name=message["from"].get("first_name"),
        last_name=message["from"].get("last_name"),
    )

    if user.is_blocked:
        await bot.sendMessage(chat_id, "🚫 You are blocked.")
        return

    if text:
        if text.startswith("/"):
            await command_handler(bot, chat_id, text, user_service)
        else:
            await handle_ai_message(bot, chat_id, text, user_service)
    else:
        await bot.sendMessage(chat_id, "i just handle text message 💔💔")
