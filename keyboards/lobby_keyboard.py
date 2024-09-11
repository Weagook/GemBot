from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_lobby_keyboard():
    play_button = InlineKeyboardButton(text='PLAY✈️', callback_data='play')
    bonus_button = InlineKeyboardButton(text='Bonus🎁', callback_data='bonus')
    leaderboard_button = InlineKeyboardButton(text='Leaderboard⭐️', callback_data='leaderboard')
    chat_button = InlineKeyboardButton(text='Chat💬', url='https://t.me/-1002288630126')
    channel_button = InlineKeyboardButton(text='Aviator King Channel', url='https://t.me/-1002239356885')
    rules_button = InlineKeyboardButton(text='Rules', callback_data='rules')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [play_button],
        [bonus_button, leaderboard_button],
        [chat_button, channel_button],
        [rules_button]
    ])

    return keyboard
