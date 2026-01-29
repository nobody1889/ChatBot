import asyncio
import httpx
from httpx import HTTPError
from .bot_client import BotClient
from .handlers.handle_updates import dispatcher
from app.core import logging

logger = logging.getLogger(__name__)

bot = BotClient()

async def polling():
    logger.info("start polling")
    offset = 0

    while True:
        try:
            updates = await bot.getUpdates(offset=offset)
            results = updates.get("result", [])

            if not results:
                continue

            for update in results:
                offset = update["update_id"] + 1
                try:
                    await dispatcher(bot, update)
                except Exception:
                    logger.exception(
                        "Error while processing update",
                        extra={"update_id": update.get("update_id")}
                    )

        except httpx.TimeoutException:
            logger.warning("Telegram polling timeout")
            await asyncio.sleep(1)

        except HTTPError:
            logger.exception("HTTP error during Telegram polling")
            await asyncio.sleep(2)

        except Exception:
            logger.exception("Unexpected error in polling loop")
            await asyncio.sleep(2)
