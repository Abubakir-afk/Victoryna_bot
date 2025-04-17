from aiogram import Bot
from aiogram.types import BotCommand

async def set_bot_menu(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Botni ishga tushirish!"),
        BotCommand(command="/help", description="Bot haqida, Yordam"),
    ]
    await bot.set_my_commands(commands)