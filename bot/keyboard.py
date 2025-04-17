from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

level_1 = KeyboardButton(text="LEVEL 1️⃣")
level_2 = KeyboardButton(text="LEVEL 2️⃣")
level_3 = KeyboardButton(text="LEVEL 3️⃣")
level_4 = KeyboardButton(text="LEVEL 4️⃣")

level_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [level_1, level_2],
        [level_3, level_4]
    ],resize_keyboard=True
)