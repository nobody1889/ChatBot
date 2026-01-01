async def start_command(bot, chat_id: str):
    await bot.sendMessage(chat_id, "wellcome to chatbot")

async def help_command(bot, chat_id: str):
    await bot.sendMessage(chat_id, "I'm a Ai bot. plz tell me what you need?")
    

COMMANDS = {
    "/start": start_command,
    "/help": help_command,
}

async def command_handler(bot, chat_id: str, text: str):
    cmd = text.split()[0]

    if cmd in COMMANDS:
        await COMMANDS[cmd](bot, chat_id)
    else:
        await bot.sendMessage(chat_id, "Unknown command.")