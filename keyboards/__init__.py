from .next_keyboard import create_next_keyboard

def create_keyboards() -> dict:
    all_keyboards = {}

    all_keyboards['next_keyboard'] = create_next_keyboard()

    return all_keyboards

KEYBOARDS = create_keyboards()

__all__ = ['KEYBOARDS']