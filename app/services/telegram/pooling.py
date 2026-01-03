from .bot_client import BotClient
from .handlers.handle_updates import dispatcher
from app.core import logging

logger = logging.getLogger(__name__)

bot = BotClient()

async def pooling():
    logger.info("start pooling")
    offset = 0

    while True:
        updates = await bot.getUpdates(offset=offset)

        results = updates.get("result", [])

        for update in results:
            offset = update["update_id"] + 1
            await dispatcher(bot, update)
