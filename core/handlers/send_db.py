from aiogram import Bot
from aiogram.types import FSInputFile
from datetime import date
from core.config import get_config

async def send_database(bot: Bot):
    await bot.send_document(get_config(".env").ADMIN_ID, document=FSInputFile(path=f"./{date.today()}.sql"), caption=f"Вот <b>База данных</b> за {date.today()}")