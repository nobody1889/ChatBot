from app.services.telegram.handlers.bot_client import BotClient
from app.services.telegram.handlers.gateways import AssistantHandler

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
                [
                # {"text": "users", "switch_inline_query_current_chat": "users_list: "},
                {"text": "assistants", "switch_inline_query_current_chat": "assistants_list: "}
                ],
            ]
        }
        )

async def new_chat_command(bot: BotClient, chat_id: str):
    await bot.sendMessage(
        chat_id=chat_id,
        text="choose the topic:",
        reply_markup={
            "inline_keyboard": [
                [
                # {"text": "users", "callback_data": "new_user_chat: "},
                {"text": "assistants", "switch_inline_query_current_chat": "new_assistant_chat: "}
                ],
            ]
        }
        )

async def select_assistant_command(bot: BotClient, chat_id: str, assistant_name: str):
    assistant = AssistantHandler(bot=bot)
    resp = await assistant.set_or_add_assistant(user_id=chat_id, assistant_name=assistant_name)

    if resp:
        await bot.sendMessage(chat_id, f"Assistant {assistant_name} selected.")
    else:
        await bot.sendMessage(chat_id, f"Failed to select assistant {assistant_name}. Please try again later.")

async def select_user_command(bot: BotClient, chat_id: str, user_name: str):
    pass

TELEGRAM_COMMANDS = {
    "/start": start_command,
    "/help": help_command,
    "/mylist": list_command,
    "/new_chat": new_chat_command,
}

SELECT_COMMANDS = {
    "/select_assistant": select_assistant_command,
    "/select_user": select_user_command,
}

async def command_handler(bot, chat_id: str, text: str):
    cmd = text.split()[0]

    if cmd in TELEGRAM_COMMANDS:
        await TELEGRAM_COMMANDS[cmd](bot, chat_id)

    elif cmd in SELECT_COMMANDS and len(text.split(" ")) > 1:
        await SELECT_COMMANDS[cmd](bot, chat_id, text.split()[1])

    else:
        await bot.sendMessage(chat_id, "Unknown command.")