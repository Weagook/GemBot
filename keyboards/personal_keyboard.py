from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_personal_keyboard():
    button1 = InlineKeyboardButton(text='PLAY✈️', callback_data='play')
    button2 = InlineKeyboardButton(text='Lobby👑', callback_data='lobby')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button1],
        [button2]
    ])

    return keyboard
