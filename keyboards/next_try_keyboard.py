from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_try_keyboard():
    next_button = InlineKeyboardButton(text='Next try', callback_data='play')
    lobby_button = InlineKeyboardButton(text='Lobby👑', callback_data='lobby')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[next_button], [lobby_button]])

    return keyboard