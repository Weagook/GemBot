from .personal_link import generate_personal_link
from .leaderboard import get_leaderboard
from .parser import parse_arguments

referal_link = generate_personal_link

__all__ = ['referal_link', 'get_leaderboard', 'parse_arguments']