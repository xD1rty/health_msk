from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.keyboards.markup import moscow_country_menu, moscow_health_menu, moscow_sex_menu
from core.states.create_health import Health
from core.db.main import Database

async def get_country(msg: Message, state: FSMContext):
    await msg.answer("🌎 Выберите ваш АО", reply_markup=moscow_country_menu)
    await state.set_state(Health.country)

async def get_health(msg: Message, state: FSMContext):
    await state.update_data(country=msg.text)
    await msg.answer("🤒 Выберите ваше состояние", reply_markup=moscow_health_menu)
    await state.set_state(Health.health)

async def get_sex(msg: Message, state: FSMContext):
    await state.update_data(health=msg.text)
    await msg.answer("👋 Выберите ваш пол", reply_markup=moscow_sex_menu)
    await state.set_state(Health.sex)

async def get_age(msg: Message, state: FSMContext):
    await state.update_data(sex=msg.text)
    await msg.answer("Введите ваш возраст")
    await state.set_state(Health.age)

async def get_height(msg: Message, state: FSMContext):
    try:
        age = int(msg.text)
    except TypeError:
        await msg.answer("Нет!!! Введи числом".replace("!", "\!"))
        return
    
    await state.update_data(age=age)
    await msg.answer("Введите ваш рост в сантиметрах")
    await state.set_state(Health.height)

async def TheEND(msg: Message, state: FSMContext):
    try:
        height = int(msg.text)
    except TypeError:
        await msg.answer("Введи числом")
        return
    db = Database()
    data = await state.get_data()
    db.create(
        telegram_id=msg.from_user.id,
        country=data["country"],
        health=data["health"],
        age=data["age"],
        sex=data["sex"],
        height=height
    )
    await msg.answer(f"""
Ваши данные:
Округ: *{data["country"]}*
Состояние: *{data['health']}*
Возраст: *{data['age']}*
Пол: *{data['sex']}*
Рост: *{height} см.*""".replace("!", "\!"))
    await state.clear()