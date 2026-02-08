from app.services.telegram.bot_client import BotClient

async def start_command(bot: BotClient, chat_id: str):
    await bot.sendMessage(chat_id, "Welcome to the chatbot 👋")

async def help_command(bot: BotClient, chat_id: str):
    await bot.sendMessage(chat_id, "I'm an AI bot 🤖. Tell me what you need!")
    
async def list_command(bot: BotClient, chat_id: str):
    await bot.sendMessage(
        chat_id=chat_id,
        text="choose the topic:",
        reply_markup={
            "inline_keyboard": [
                [{"text": "users", "switch_inline_query_current_chat": "users_list: "},
                {"text": "assistants", "switch_inline_query_current_chat": "assistants_list: "}],
            ]
        }
        )

async def new_chat_command(bot: BotClient, chat_id: str):
    await bot.sendMessage(
        chat_id=chat_id,
        text="choose the topic:",
        reply_markup={
            "inline_keyboard": [
                [{"text": "users", "callback_data": "new_user_chat: "},
                {"text": "assistants", "switch_inline_query_current_chat": "new_assistant_chat: "}],
            ]
        }
        )

COMMANDS = {
    "/start": start_command,
    "/help": help_command,
    "/mylist": list_command,
    "/new_chat": new_chat_command
}

async def command_handler(bot, chat_id: str, text: str):
    cmd = text.split()[0]

    if cmd in COMMANDS:
        await COMMANDS[cmd](bot, chat_id)
    else:
        await bot.sendMessage(chat_id, "Unknown command.")