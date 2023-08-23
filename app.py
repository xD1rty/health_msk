# 😀🔥👾🤖👻☠️🤒😵‍💫🥱🫠😖👨‍💻🧑‍💻👩‍💻🍃🌎🪐🌝🌚⛅️📲💻🩻🎮👋

from aiogram import Bot, Dispatcher, F
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
from core.handlers.startup import startup_bot
from core.handlers.shutdown import shutdown_bot
from core.handlers.commands import get_start
from core.utils.commands import set_commands
from core.states.create_health import Health
from core.handlers.get_health import get_user_health
from core.config import get_config
from core.handlers.create_health import get_age, get_country, get_health, get_height, get_sex, TheEND
from core.handlers.send_db import send_database
import logging
import asyncio
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    bot = Bot(token=get_config(".env").BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    await set_commands(bot)
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(send_database, trigger="cron", hour=11, minute=48, start_date=datetime.now(), kwargs={
        "bot": bot
    })
    scheduler.start()
    dp.startup.register(startup_bot)
    dp.shutdown.register(shutdown_bot)
    dp.message.register(get_start, Command("start"))
    dp.message.register(get_country, F.text == "🤒 Добавить состояние за сегодня")
    dp.message.register(get_health, Health.country)
    dp.message.register(get_sex, Health.health)
    dp.message.register(get_age, Health.sex)
    dp.message.register(get_height, Health.age)
    dp.message.register(TheEND, Health.height)
    dp.message.register(get_user_health, F.text == "💻 Состояние сегодня")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())