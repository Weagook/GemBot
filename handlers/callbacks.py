from aiogram import Router, Bot
from aiogram.types import CallbackQuery
from bot_manager import BotManager
from keyboards import KEYBOARDS
from database.async_database import AsyncDatabase
from utils import referal_link
import events
from config import IMAGES, VIDEO, ANIMATION
from random import randint

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

lobby_message = '''👑LOBBY👑

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

payout_info_message = '''Why do we transfer payouts to a crypto wallet? Payouts in cryptocurrency have the following advantages:

✅ Instant payouts with no delays
✅ Your money is always secure and accessible only to you
✅ No banking fees
✅ USDT can be converted to any currency and used instantly
✅ Payouts are available to any crypto wallets. Payouts are made to accounts opened in USDT (TRC20)
✅ We recommend registering with the most popular crypto wallets: Binance Wallet, Coinbase Wallet, ByBit Wallet, and other

✉️In case you rank in the weekly TOP-10 players, our manager will contact you to request your account number for the payout. The login of our manager is: @AviatorKingManager'''

bot = BotManager()
router = Router()
db = AsyncDatabase()

@router.callback_query()
async def handle_callback(query: CallbackQuery):
    user_id = query.from_user.id
    if query.data == 'next_button':
        await bot.send_animation(chat_id=user_id, animation=ANIMATION['next'], caption=trial_message_1, reply_markup=KEYBOARDS['trial_keyboard_1'])
    if query.data == 'trial_1':
        await bot.send_animation(chat_id=user_id, animation=ANIMATION['next_try'], caption=trial_message_2, reply_markup=KEYBOARDS['trial_keyboard_2'])
    if query.data == 'trial_2':
        await bot.send_animation(chat_id=user_id, animation=ANIMATION['x5'], caption=trial_message_3, reply_markup=KEYBOARDS['trial_keyboard_3'])
    if query.data == 'trial_3':
        await bot.send_animation(chat_id=user_id, animation=ANIMATION['next_try'], caption=trial_message_4, reply_markup=KEYBOARDS['trial_keyboard_4'])
    if query.data == 'trial_4':
        await bot.send_animation(chat_id=user_id, animation=ANIMATION['x3'], caption=trial_message_5, reply_markup=KEYBOARDS['trial_keyboard_5'])
    if query.data == 'trial_5':
        await bot.send_message(chat_id=user_id, text=trial_message_6, reply_markup=KEYBOARDS['trial_keyboard_6'])
    if query.data in ['trial_x3', 'trial_x5', 'trial_x10']:
        imgs = ['trial_x3', 'trial_x5', 'trial_x10']
        imgs.remove(query.data)
        index = imgs[randint(1, 2)-1]
        await bot.send_animation(chat_id=user_id, animation=ANIMATION[index.split('_')[1]], caption=trial_message_7, reply_markup=KEYBOARDS['complete_tutorial'])
    if query.data in ['complete_tutorial', 'back', 'lobby']:
        await events.entry_lobby(bot, IMAGES['lobby'], db, user_id, lobby_message, KEYBOARDS)
    if query.data == 'bonus':
        referal_link = await db.get_user_property(telegram_id=user_id, property_name='referral_link')
        cur_message = bonus_message.replace('[REFERRAL_LINK]', referal_link)
        await bot.send_photo(chat_id=user_id, photo=IMAGES['bonus'], caption=cur_message, reply_markup=KEYBOARDS['bonus'])
    if query.data == 'personal_link':
        await events.entry_personal(bot, db, user_id, personal_message, KEYBOARDS)
    if query.data == 'your_referrals':
        await events.entry_referrals(bot, db, user_id, refferal_message, KEYBOARDS)
    if query.data == 'play':
        await events.entry_choice_play(bot, user_id, KEYBOARDS)
    if query.data == 'leaderboard':
        await events.entry_leaderboard(bot, IMAGES['leaderboard'], db, user_id, KEYBOARDS)
    if query.data in ['play_x3', 'play_x5', 'play_x10']:
        await events.play_roll(bot, db, user_id, KEYBOARDS, query)
    if query.data == 'payout_info':
        await events.entry_payout_info(bot, IMAGES['payout_info'], db, user_id, payout_info_message, KEYBOARDS)
    if query.data == 'next_try':
        await events.entry_choice_play(bot, user_id, KEYBOARDS)
    if query.data == 'rules':
        await bot.send_message(chat_id=user_id, text=trial_message_1, reply_markup=KEYBOARDS['rules'])
