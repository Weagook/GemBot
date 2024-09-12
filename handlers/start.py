from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from states import ALL_STATES
from utils import referal_link, parse_arguments
from database.async_database import AsyncDatabase
from keyboards import KEYBOARDS
from events import entry_lobby
from bot_manager import BotManager
from config import IMAGES


router = Router()
db = AsyncDatabase()
bot = BotManager()


start_message_text = '''Enter your name, it will be displayed in the Aviator King leaderboard of winners✈️'''
lobby_message = '''👑LOBBY👑

Hello, [NAME]!

Points: [POINTS]
Spins remaining: [SPINS] / 30
Your status: [STATUS]

Claim your guaranteed welcome bonus of $1 by spinning your first 5 spins'''


@router.message(Command('start'))
async def start_command(message: Message, state: FSMContext, command: CommandObject):
    args = command.args
    inviter_id, tag = parse_arguments(args)

    if inviter_id:
        inviter_id = int(inviter_id)

    name = message.from_user.username
    user_id = message.from_user.id
    refferal_link = referal_link(user_id=user_id)

    user_exists = await db.user_exists(telegram_id=user_id)

    if user_exists:
        await entry_lobby(bot, IMAGES['lobby'], db, user_id, lobby_message, KEYBOARDS)
        return

    res_execute = await db.add_user(telegram_id=user_id, name=name, tag=tag, refferal_link=refferal_link, inviter_id=inviter_id)

    await state.set_state(ALL_STATES['register'].waiting_input_name)
    await message.answer_photo(photo=IMAGES['get_name'], caption=start_message_text)