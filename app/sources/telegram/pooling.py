from .bot_client import BotClient
from handlers import handle_updates

bot = BotClient()

async def pooling():
    offeset = 0
    updates, offeset = await bot.getUpdates(offset=offeset)
    await handle_updates(bot, updates)