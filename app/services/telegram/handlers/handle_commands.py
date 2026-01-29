from app.services.telegram.bot_client import BotClient
from app.schemas import  UserRead

async def start_command(bot: BotClient, chat_id: str):
    await bot.sendMessage(chat_id, f"wellcome to chatbot")

async def help_command(bot: BotClient, chat_id: str):
    await bot.sendMessage(chat_id, "I'm a Ai bot. plz tell me what you need?")
    
async def list_command(bot: BotClient, chat_id: str):
    await bot.sendMessage(
        chat_id=chat_id,
        text="choose the topic:",
        reply_markup={
            "inline_keyboard": [
                [{"text": "users", "callback_data": "users_list"}],
                [{"text": "assistants", "callback_data": "assistants_list"}],
            ]
        }
        )

async def new_chat_command(bot: BotClient, chat_id: str):
    await bot.sendMessage(
        chat_id=chat_id,
        text="choose the topic:",
        reply_markup={
            "inline_keyboard": [
                [{"text": "users", "callback_data": "new_user_chat"}],
                [{"text": "assistants", "callback_data": "new_assistant_chat"}],
            ]
        }
        )

COMMANDS = {
    "/start": start_command,
    "/help": help_command,
    "/MyList": list_command,
    "/NewChat": new_chat_command
}

async def command_handler(bot, chat_id: str, text):
    cmd = text.split()[0]

    if cmd in COMMANDS:
        await COMMANDS[cmd](bot, chat_id)
    else:
        await bot.sendMessage(chat_id, "Unknown command.")