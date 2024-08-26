from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_bonus_keyboard():
    button1 = InlineKeyboardButton(text='Personal link🤝', callback_data='personal_link')
    button2 = InlineKeyboardButton(text='Your referrals💪', callback_data='your_referrals')
    button3 = InlineKeyboardButton(text='PLAY✈️', callback_data='play')
    button4 = InlineKeyboardButton(text='Lobby👑', callback_data='lobby')
    button5 = InlineKeyboardButton(text='How to receive a payout💰', callback_data='payout_info')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button1],
        [button2],
        [button3],
        [button4],
        [button5]
    ])

    return keyboard
