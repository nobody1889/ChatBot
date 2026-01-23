from app.services.assistant import AssistantClient as AiClient
from app.core.logging import logging

logger = logging.getLogger(__name__)

async def handle_ai_message(bot, chat_id, message):
    ai = AiClient()
    try:
        logger.info(f"ai client created for chat_from: {chat_id} and message: {message}",)
        response = await ai.chat(message=message)
        response = await bot.sendMessage(chat_id, response)
    except Exception as e:
        logger.error(e)
    finally:
        await ai.close()
        logger.info("ai client closed")

