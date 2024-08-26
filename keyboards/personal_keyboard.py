from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_personal_keyboard():
    button1 = InlineKeyboardButton(text='PLAY✈️', callback_data='play')
    button2 = InlineKeyboardButton(text='Lobby👑', callback_data='lobby')
    button3 = InlineKeyboardButton(text='Back↩️', callback_data='back')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button1],
        [button2],
        [button3]
    ])

    return keyboard
