from aiogram import Router, Bot
from aiogram.types import CallbackQuery
from bot_manager import BotManager
from keyboards import KEYBOARDS

IMAGE_ID = 'AgACAgIAAxkBAAMdZsZcHwTsyBWs5I89uop-Xu2hYBgAArnbMRsr_DlKxGHQvWtGL38BAAMCAAN4AAM1BA'
trial_message_1 = '''"The King shares the simple rules for the top aviators' race:

💎 30 free spins to conquer the Sky
💎 If you guess the height the plane will reach, your spins won't be deducted, and the victory will go towards your ranking. If you don't guess correctly, you'll still have 29 more attempts to continue.
💎 Each correct guess gives you +1 point
💎 The ranking for the current day is formed daily at 23:59
💎 The final ranking for the current week is formed weekly at 23:59
💎 The list of winners is published weekly on the Aviator King channel
💎 We pay out winnings to any wallet (USDT)
💎 Free spins are refreshed daily at 00:00. Play regularly and claim your prizes!

Shall we try it now?"'''


bot = BotManager()
router = Router()

@router.callback_query()
async def handle_callback(query: CallbackQuery):
    user_id = query.from_user.id
    if query.data == "next_button":
        await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=trial_message_1, reply_markup=KEYBOARDS['trial_keyboard_1'])
