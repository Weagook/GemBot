from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_trial_kb_1():
    button = InlineKeyboardButton(text='Trial', callback_data='trial_1')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    return keyboard


def create_trial_kb_2():
    button = InlineKeyboardButton(text='x5', callback_data='trial_2')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    return keyboard


def create_trial_kb_3():
    button = InlineKeyboardButton(text='Next try', callback_data='trial_3')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    return keyboard


def create_trial_kb_4():
    button = InlineKeyboardButton(text='x3', callback_data='trial_4')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    return keyboard

def create_trial_kb_5():
    button = InlineKeyboardButton(text='Next try', callback_data='trial_5')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    return keyboard


def create_trial_kb_6():
    button1 = InlineKeyboardButton(text='x3', callback_data='trial_6')
    button2 = InlineKeyboardButton(text='x5', callback_data='trial_6')
    button3 = InlineKeyboardButton(text='x10', callback_data='trial_6')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button1, button2, button3]])
    return keyboard