from aiogram.fsm.state import State, StatesGroup

class Health(StatesGroup):
    country = State()
    health = State()
    age = State()
    sex = State()
    height = State()