from aiogram import Router, Bot
from aiogram.types import CallbackQuery
from bot_manager import BotManager
from keyboards import KEYBOARDS
from database import DATABASE
from utils import referal_link
import events

IMAGE_ID = 'AgACAgIAAxkBAAMdZsZcHwTsyBWs5I89uop-Xu2hYBgAArnbMRsr_DlKxGHQvWtGL38BAAMCAAN4AAM1BA'
trial_message_1 = '''The King shares the simple rules for the top aviators' race:

💎 30 free spins to conquer the Sky
💎 If you guess the height the plane will reach, your spins won't be deducted, and the victory will go towards your ranking. If you don't guess correctly, you'll still have 29 more attempts to continue.
💎 Each correct guess gives you +1 point
💎 The ranking for the current day is formed daily at 23:59
💎 The final ranking for the current week is formed weekly at 23:59
💎 The list of winners is published weekly on the Aviator King channel
💎 We pay out winnings to any wallet (USDT)
💎 Free spins are refreshed daily at 00:00. Play regularly and claim your prizes!

Shall we try it now?'''

trial_message_2 = '''What does your intuition tell you? How high will the plane fly?
No doubt, luck will be on your side!'''

trial_message_3 = '''✅✅✅
You won! Great job, keep it up!💪'''

trial_message_4 = '''How high will the plane fly?'''

trial_message_5 = '''✅✅✅
You won! Great job, keep it up!💪'''

trial_message_6 = '''What will you choose this time?✈️✈️✈️

The King is pleased with your success!'''

trial_message_7 = '''❌❌❌
Unsuccessful attempt, but no worries, you'll get it next time!'''

complete_tutorial_message = '''👑LOBBY👑

Hello, [NAME]!

Points: [POINTS]
Spins remaining: [SPINS] / 30
Your status: [STATUS]

Claim your guaranteed welcome bonus of $1 by spinning your first 5 spins'''

bonus_message = '''
💎100 friends - Platinum status +10 spins DAILY💎
🏅50 friends - Gold status +5 spins DAILY🏅
🥈10 friends - Silver status +3 spins DAILY🥈
🥉3 friends - Bronze status +1 spin DAILY🥉
🥲0 friends - Player status +0 spins DAILY🥲

Share your personal link with friends in CHATS and SOCIAL MEDIA, increase your rank, and win money!
[REFERRAL_LINK]

Your status will change depending on the number of friends you bring. Only a few will become Kings. Maybe you'll be the King?
'''

personal_message = '''Here is your personal link:

[REFERRAL_LINK]

You will receive a notification when your referral joins the game🎫

Share the link in chats and social media to earn as much as possible! 💵'''

refferal_message = '''Your referrals are displayed here:
[PLACEHOLDER]'''

bot = BotManager()
router = Router()

@router.callback_query()
async def handle_callback(query: CallbackQuery):
    user_id = query.from_user.id
    if query.data == 'next_button':
        await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=trial_message_1, reply_markup=KEYBOARDS['trial_keyboard_1'])
    if query.data == 'trial_1':
        await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=trial_message_2, reply_markup=KEYBOARDS['trial_keyboard_2'])
    if query.data == 'trial_2':
        await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=trial_message_3, reply_markup=KEYBOARDS['trial_keyboard_3'])
    if query.data == 'trial_3':
        await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=trial_message_4, reply_markup=KEYBOARDS['trial_keyboard_4'])
    if query.data == 'trial_4':
        await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=trial_message_5, reply_markup=KEYBOARDS['trial_keyboard_5'])
    if query.data == 'trial_5':
        await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=trial_message_6, reply_markup=KEYBOARDS['trial_keyboard_6'])
    if query.data == 'trial_6':
        await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=trial_message_7, reply_markup=KEYBOARDS['complete_tutorial'])
    if query.data in ['complete_tutorial', 'back', 'lobby']:
        await events.entry_lobby(bot, IMAGE_ID, DATABASE, user_id, complete_tutorial_message, KEYBOARDS)
    if query.data == 'bonus':
        referal_link = DATABASE.get_link(user_id)
        cur_message = bonus_message.replace('[REFERRAL_LINK]', referal_link)
        await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=cur_message, reply_markup=KEYBOARDS['bonus'])
    if query.data == 'personal_link':
        await events.entry_personal(bot, IMAGE_ID, DATABASE, user_id, personal_message, KEYBOARDS)
    if query.data == 'your_referrals':
        await events.entry_referrals(bot, IMAGE_ID, DATABASE, user_id, refferal_message, KEYBOARDS)
    if query.data == 'play':
        await events.entry_choice_play(bot, DATABASE, user_id, IMAGE_ID, KEYBOARDS)
    if query.data == 'leaderboard':
        await events.entry_leaderboard(bot, IMAGE_ID, DATABASE, user_id, KEYBOARDS)
    if query.data in ['play_x3', 'play_x5', 'play_x10']:
        await events.play_roll(bot, DATABASE, user_id, KEYBOARDS, query)
        
        
