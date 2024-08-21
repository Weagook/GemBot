from aiogram.fsm.state import State, StatesGroup

class RegistrationState(StatesGroup):
    waiting_input_name = State()