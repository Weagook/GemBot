from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def create_play_game():
    button1 = InlineKeyboardButton(text='x3', callback_data='play_x3')
    button2 = InlineKeyboardButton(text='x5', callback_data='play_x5')
    button3 = InlineKeyboardButton(text='x10', callback_data='play_x10')
    button4 = InlineKeyboardButton(text='Back↩️', callback_data='back')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button1, button2, button3], [button4]])
    return keyboard