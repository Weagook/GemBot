from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from database import DATABASE
from keyboards import KEYBOARDS
from states import ALL_STATES


router = Router()

IMAGE_ID = 'AgACAgIAAxkBAAMdZsZcHwTsyBWs5I89uop-Xu2hYBgAArnbMRsr_DlKxGHQvWtGL38BAAMCAAN4AAM1BA'
name_message = '''Hello [NAME]! The King has sent his message✉️
By the order of the reigning Aviator King:
Weekly payouts will be given to the top 10 pilots who can soar the highest! Payouts will be made to a crypto wallet (USDT)
💰 1st place — $5
💰 2nd place — $4
💰 3rd place — $3
💰 4th-10th place — $1
Claim your GUARANTEED welcome bonus by spinning your first 5 free spins!'''


@router.message(StateFilter(ALL_STATES['register'].waiting_input_name))
async def start_command(message: Message, state: FSMContext):
    await state.clear()
    DATABASE.add_user_name(message.from_user.id, message.text)
    replace_name_message = name_message.replace('[NAME]', message.text)
    await message.answer_photo(photo=IMAGE_ID, caption=replace_name_message, reply_markup=KEYBOARDS['next_keyboard'])