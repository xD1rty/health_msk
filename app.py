from aiogram import Bot, Dispatcher
from core.handlers.startup import startup_bot
import asyncio

async def start():
    bot = Bot(token="")
    dp = Dispatcher()

    dp.startup.register(startup_bot)