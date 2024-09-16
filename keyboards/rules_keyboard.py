from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_rules_keyboard():
    next_button = InlineKeyboardButton(text='PLAY✈️', callback_data='play')
    lobby_button = InlineKeyboardButton(text='Lobby👑', callback_data='lobby')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[next_button], [lobby_button]])

    return keyboard