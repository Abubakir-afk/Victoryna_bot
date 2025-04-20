import os
import random

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from bot.keyboard import level_buttons

router = Router()

@router.message(CommandStart())
async def command_start(message: Message):
    from_user = message.from_user
    first_name = from_user.first_name
    last_name = from_user.last_name
    full_name = f"{first_name} {last_name if last_name else ''}"
    # full_name = f"{message.from_user.first_name}"
    await message.answer(f"Salom {full_name}, bizning Viktorina botimizga xush kelibsiz! )")
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.jpg"))
    text = f"Xush kelibsiz {full_name} bilag'on, biz sizga bir nechta savollar berib bilimingizni tekshitib beramiz!"
    await message.answer_photo(photo=img, caption=text, reply_markup=level_buttons)

@router.message(F.text == "LEVEL 1️⃣")
async def level_1(message: Message):
    question = (f"{random.randint(15, 50)} {random.choice(['+','-','*'])}"
                f"{random.randint(15, 50)}")
    await message.answer(text=f"Savol: {question} = ?")

@router.message(F.text == "LEVEL 2️⃣")
async def level_2(message: Message):
    question = (f"{random.randint(70, 140)} {random.choice(['+','-','*'])}"
                f"{random.randint(70, 140)}")
    await message.answer(text=f"Savol: {question} = ?")

@router.message(F.text == "LEVEL 3️⃣")
async def level_3(message: Message):
    question = (f"{random.randint(150, 280)} {random.choice(['+','-','*'])}"
                f"{random.randint(150, 280)}")
    await message.answer(text=f"Savol: {question} = ?")

@router.message(F.text == "LEVEL 4️⃣")
async def level_1(message: Message):
    question = (f"{random.randint(310, 520)} {random.choice(['+','-','*'])}"
                f"{random.randint(310, 520)}")
    await message.answer(text=f"Savol: {question} = ?")