from aiogram import Bot
from aiogram.types import Message

async def get_start(msg: Message, bot: Bot):
    await msg.answer(f"""
Привет, {msg.from_user.first_name} 👋
Мы собираем данные здоровья людей города Москва 👨
Плохо или хорошо сегодня себя чувствовал? 🥱
Добавь эти данные в нашего бота 🤖

*❗️ БОТ СДЕЛАН В ОЗНАКОМИТЕЛЬНЫХ ЦЕЛЯХ ❗️️*""")