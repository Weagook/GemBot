from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_next_keyboard():
    next_button = InlineKeyboardButton(text='Next', callback_data='next_button')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[next_button]])

    return keyboard