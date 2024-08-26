from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_lobby_keyboard():
    play_button = InlineKeyboardButton(text='PLAY✈️', callback_data='play')
    bonus_button = InlineKeyboardButton(text='Bonus🎁', callback_data='bonus')
    leaderboard_button = InlineKeyboardButton(text='Leaderboard⭐️', callback_data='leaderboard')
    chat_button = InlineKeyboardButton(text='Chat💬', callback_data='chat')
    channel_button = InlineKeyboardButton(text='Aviator King Channel', callback_data='channel')
    rules_button = InlineKeyboardButton(text='Rules', callback_data='rules')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [play_button],
        [bonus_button, leaderboard_button],
        [chat_button, channel_button],
        [rules_button]
    ])

    return keyboard
