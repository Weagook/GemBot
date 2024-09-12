from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_trial_kb_1():
    button = InlineKeyboardButton(text="Let's try", callback_data='trial_1')
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
    button1 = InlineKeyboardButton(text='x3', callback_data='trial_x3')
    button2 = InlineKeyboardButton(text='x5', callback_data='trial_x5')
    button3 = InlineKeyboardButton(text='x10', callback_data='trial_x10')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button1, button2, button3]])
    return keyboard

def create_complete_kb():
    button = InlineKeyboardButton(text='Next try', callback_data='complete_tutorial')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    return keyboard