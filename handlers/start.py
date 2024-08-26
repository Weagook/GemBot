from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import ALL_STATES
from database import DATABASE


router = Router()


IMAGE_ID = 'AgACAgIAAxkBAAMdZsZcHwTsyBWs5I89uop-Xu2hYBgAArnbMRsr_DlKxGHQvWtGL38BAAMCAAN4AAM1BA'
start_message_text = '''Enter your name, it will be displayed in the Aviator King leaderboard of winners✈️'''


@router.message(Command('start'))
async def start_command(message: Message, state: FSMContext, command: Command):
    referal_code = command.args
    if referal_code:
        if DATABASE.is_exists(referal_code):
            DATABASE.add_follower(referal_code, message.from_user.id)
    
    if not DATABASE.is_exists(message.from_user.id):
        DATABASE.add_user_by_id(message.from_user.id)

    await state.set_state(ALL_STATES['register'].waiting_input_name)
    await message.answer_photo(photo=IMAGE_ID, caption=start_message_text)