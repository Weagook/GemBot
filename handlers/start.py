from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import DATABASE


router = Router()


start_message_text = '''Enter your name, it will be displayed in the Aviator King leaderboard of winners✈️'''


@router.message(Command('start'))
async def start_command(message: Message):
    DATABASE.add_user_by_id(message.from_user.id)
    await message.answer(start_message_text)