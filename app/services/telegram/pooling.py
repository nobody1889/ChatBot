from .bot_client import BotClient
from .handlers.handle_updates import dispatcher
from app.core import logging
from app.db.session import async_sessionLocal
from accounts.user_repository import UserRepository
from accounts.user_service import UserService

logger = logging.getLogger(__name__)

bot = BotClient()

async def polling():
    logger.info("start polling")
    offset = 0

    while True:
        updates = await bot.getUpdates(offset=offset)
        results = updates.get("result", [])

        if not results:
            continue

        async with async_sessionLocal() as db:
            repo = UserRepository(db)
            service = UserService(repo)

            for update in results:
                offset = update["update_id"] + 1
                await dispatcher(bot, update, service)

            await db.commit()
