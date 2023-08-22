from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🤒 Добавить состояние за сегодня"),
            KeyboardButton(text="💻 Состояние сегодня")
        ],
        [
            KeyboardButton(text="Админ бота")
        ]
    ],
    resize_keyboard=True
)

moscow_country_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ЦАО")
        ],
        [
            KeyboardButton(text="САО")
        ],
        [
            KeyboardButton(text="СВАО")
        ],
        [
            KeyboardButton(text="ВАО")
        ],
        [
            KeyboardButton(text="ЮВАО")
        ],
        [
            KeyboardButton(text="ЮАО")
        ],
        [
            KeyboardButton(text="ЮЗАО")
        ],
        [
            KeyboardButton(text="ЗАО")
        ],
        [
            KeyboardButton(text="СЗАО")
        ],
        [
            KeyboardButton(text="Зеленоград")
        ],
        [
            KeyboardButton(text="НАО")
        ],
        [
            KeyboardButton(text="ТАО")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

moscow_health_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Супер"),
            KeyboardButton("Отлично!")
        ],
        [
            KeyboardButton("Хорошо"),
            KeyboardButton("Приемлимо")
        ],
        [
            KeyboardButton("Плохо"),
            KeyboardButton("Фигово")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)