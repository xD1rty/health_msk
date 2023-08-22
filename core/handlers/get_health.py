from aiogram.types import Message
from core.db.main import Database
from datetime import date
async def get_user_health(msg: Message):
    data = Database().get_by_id(msg.from_user.id)
    if not data:
        await msg.answer("За сегодня вашего состояния нет :(")
        return

    await msg.answer(f"""
Ваше состояние за {date.today()}
Округ: {data[2]}
Состояние: {data[3]}
Возраст: {data[4]}
Пол: {data[5]}
Рост: {data[6]}
""")