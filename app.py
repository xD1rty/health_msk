from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from core.handlers.startup import startup_bot
from core.config import get_config
import logging
import asyncio

async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    bot = Bot(token=get_config(".env").BOT_TOKEN, parse_mode=ParseMode.MARKDOWN_V2)
    dp = Dispatcher()

    dp.startup.register(startup_bot)
    dp.shutdown.register(startup_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())