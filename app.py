# 😀🔥👾🤖👻☠️🤒😵‍💫🥱🫠😖👨‍💻🧑‍💻👩‍💻🍃🌎🪐🌝🌚⛅️📲💻🩻🎮👋

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
from core.handlers.startup import startup_bot
from core.handlers.shutdown import shutdown_bot
from core.handlers.commands import get_start
from core.utils.commands import set_commands
from core.config import get_config
import logging
import asyncio

async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    bot = Bot(token=get_config(".env").BOT_TOKEN, parse_mode=ParseMode.MARKDOWN_V2)
    dp = Dispatcher()
    await set_commands(bot)
    dp.startup.register(startup_bot)
    dp.shutdown.register(shutdown_bot)
    dp.message.register(get_start, Command("start"))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())