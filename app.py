from aiogram import Bot, Dispatcher
from core.handlers.startup import startup_bot
from core.config import get_config
import asyncio

async def start():
    bot = Bot(token=get_config(".env").BOT_TOKEN)
    dp = Dispatcher()

    dp.startup.register(startup_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())