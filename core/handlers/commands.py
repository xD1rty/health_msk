from aiogram import Bot, html
from aiogram.types import Message

from core.keyboards.markup import main_menu

async def get_start(msg: Message, bot: Bot):
    await msg.answer(f"""
Привет, {msg.from_user.first_name} 👋
Мы собираем данные здоровья людей города Москва 👨
Плохо или хорошо сегодня себя чувствовал? 🥱
Добавь эти данные в нашего бота 🤖

{html.bold(html.quote("❗ БОТ СДЕЛАН В ОЗНАКОМИТЕЛЬНЫХ ЦЕЛЯХ ❗️️"))}""", reply_markup=main_menu)