import os
import random

from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile
from keyboard import level_buttons, start_btn
from states import LevelState
from keyboard import stop_btn

router = Router()

def get_min_max_number(level):
    # funksiyani qolgan lever uchun xam moslash kerak
    if level == "LEVEL 1️⃣":
        return 15, 50
    elif level == "LEVEL 2️⃣":
        return 70, 140

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

@router.message(F.text == "🎲Boshlash")
async def start_game(message: Message):
    await message.answer("O'yin qaytadan boshlandi!", reply_markup=level_buttons)

@router.message(F.text == "LEVEL 1️⃣")
async def level_1(message: Message, state: FSMContext):
    question = (f"{random.randint(15, 50)} {random.choice(['+', '-'])}"
                f" {random.randint(15, 50)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="LEVEL 1️⃣",
                            correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_btn)
    await state.set_state(LevelState.javob)

@router.message(F.text == "LEVEL 2️⃣")
async def level_2(message: Message, state: FSMContext):
    question = (f"{random.randint(70, 140)} {random.choice(['+', '-'])}"
                f"{random.randint(70, 140)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="LEVEL 2️⃣",
                            correct=0, incorrect=0)
    await message.answer(text=f"Savol: {question} = ?")
    await state.set_state(LevelState.javob)

@router.message(F.text == "LEVEL 3️⃣")
async def level_3(message: Message, state: FSMContext):
    question = (f"{random.randint(150, 280)} {random.choice(['+', '-', '*'])}"
                f"{random.randint(150, 280)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="LEVEL 3️⃣",
                            correct=0, incorrect=0)
    await message.answer(text=f"Savol: {question} = ?")
    await state.set_state(LevelState.javob)
@router.message(F.text == "LEVEL 4️⃣")
async def level_4(message: Message, state: FSMContext):
    question = (f"{random.randint(310, 520)} {random.choice(['+', '-', '*'])}"
                f"{random.randint(310, 520)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="LEVEL 4️⃣",
                            correct=0, incorrect=0)
    await message.answer(text=f"Savol: {question} = ?")
    await state.set_state(LevelState.javob)


@router.message(StateFilter(LevelState.javob))
async def process_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    correct_answer = data.get("answer")
    correct = data.get("correct", 0)
    incorrect = data.get("incorrect", 0)
    level = data.get("level")
    if message.text == "STOP⛔":
        text = (f"{level}\n"
                f"Savollar soni: {correct + incorrect}\n"
                f"✅To'g'ri javoblar: {correct}\n"
                f"❌Noto'g'ri javoblar: {incorrect}\n")
        await message.answer(text, reply_markup=start_btn)
        await state.clear()
        return
    try:
        user_answer = int(message.text)
        if user_answer == correct_answer:
            correct += 1
            await message.answer("✅Javob to'g'ri!")
        else:
            incorrect += 1
            await message.answer(f"❌Javob noto'g'ri!\n✅To'g'ri javob: {correct_answer}")
    except ValueError:
        await message.answer("Iltimos raqam kiriting")

    min_number, max_number = get_min_max_number(level)
    question = (f"{random.randint(min_number, max_number)}"
                f"{random.choice(['+', '-','*'])}"
                f"{random.randint(min_number, max_number)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, correct=correct, incorrect=incorrect)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_btn)