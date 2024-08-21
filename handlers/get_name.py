from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from database import DATABASE
from keyboards import KEYBOARDS


router = Router()


name_message = 'WE NEED TO COME UP WITH A TEXT'


@router.message(state='*')
async def start_command(message: Message):
    await message.answer(name_message, reply_markup=KEYBOARDS['next_keyboard'])