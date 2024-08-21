from .register import RegistrationState

def create_states() -> dict:
    ALL_STATES = {}

    ALL_STATES['register'] = RegistrationState

    return ALL_STATES

ALL_STATES = create_states()

__all__ = ['ALL_STATES']