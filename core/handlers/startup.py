from aiogram import Bot, html
from core.config import get_config

async def startup_bot(bot: Bot):
    await bot.send_message(get_config(".env").ADMIN_ID, f"{html.bold(html.quote('BOT'))} запустился и готов к работе\!")