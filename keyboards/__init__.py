from .next_keyboard import create_next_keyboard
from .trial_keyboards import *
from .lobby_keyboard import create_lobby_keyboard
from .bonus_keyboard import create_bonus_keyboard
from .personal_keyboard import create_personal_keyboard
from .play_keyboard import create_play_game

def create_keyboards() -> dict:
    all_keyboards = {}

    all_keyboards['next_keyboard'] = create_next_keyboard()
    all_keyboards['trial_keyboard_1'] = create_trial_kb_1()
    all_keyboards['trial_keyboard_2'] = create_trial_kb_2()
    all_keyboards['trial_keyboard_3'] = create_trial_kb_3()
    all_keyboards['trial_keyboard_4'] = create_trial_kb_4()
    all_keyboards['trial_keyboard_5'] = create_trial_kb_5()
    all_keyboards['trial_keyboard_6'] = create_trial_kb_6()
    all_keyboards['complete_tutorial'] = create_complete_kb()
    all_keyboards['lobby'] = create_lobby_keyboard()
    all_keyboards['bonus'] = create_bonus_keyboard()
    all_keyboards['personal'] = create_personal_keyboard()
    all_keyboards['play'] = create_play_game()

    return all_keyboards

KEYBOARDS = create_keyboards()

__all__ = ['KEYBOARDS']