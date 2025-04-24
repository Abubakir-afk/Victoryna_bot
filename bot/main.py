import asyncio
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from bot.menu import set_bot_menu
from handlers import router as handlers_router

from aiogram.client.session.aiohttp import AiohttpSession
session = AiohttpSession(proxy="http://proxy.server:3128")

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(handlers_router)

async def main() -> None:
    bot = Bot(token=TOKEN, session=session)
    await set_bot_menu(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())