from app.services.assistant import AssistantClient as AiClient
from app.core.logging import logging
from app.services.telegram.bot_client import BotClient

logger = logging.getLogger(__name__)

async def handle_ai_message(bot: BotClient, user: dict, message: str, message_id: int) -> None:
    chat_id = user.get("user_id")
    assistants: list = user.get("asstants")

    if not assistants:
        await bot.sendMessage(
            chat_id=chat_id,
            text="😔 You don't have any assistants yet\n\n"
            "Use /new_chat to create one\n"
            "Use /mylist to see your assistants",
            reply_message_id=message_id,
        )
        return

    default_assistant = assistants[0]
    ai = AiClient(assistant=default_assistant)

    try:
        logger.info(f"ai client created for chat_from: {chat_id} and message: {message}")
        response = await ai.chat(message=message)
        response = await bot.sendMessage(
            chat_id, 
            response
            
            )
    except Exception as e:
        logger.error(e)
    finally:
        await ai.close()
        logger.info("ai client closed")

