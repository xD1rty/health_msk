from aiogram import Bot
from core.config import get_config

async def startup_bot(bot: Bot):
    await bot.send_message(get_config(".env").ADMIN_ID, "<b>БОТ</b> запустился и готов к работе!")