from .handle_commands import command_handler
from app.services.assistant.handlers.text import handle_ai_message

async def dispatcher(bot, update) -> None:
    if "message" not in update:
        return

    message = update["message"]
    chat_id = message["chat"]["id"]

    if "text" in message:
        text = message["text"]
        
        if text.startswith("/"):
            await command_handler(bot, chat_id, text)

        else:
            await handle_ai_message(bot, chat_id, text)
    else:
        await bot.sendMessage(chat_id, "i just handel text message 💔💔")