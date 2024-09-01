from bot_manager import BotManager
from config import BOT_USERNAME

bot = BotManager()

def generate_personal_link(user_id, tag=None):
    if tag:
        return f"https://t.me/{BOT_USERNAME}?start=inviter_id{user_id}andtag{tag}"
    return f"https://t.me/{BOT_USERNAME}?start=inviter_id{user_id}"