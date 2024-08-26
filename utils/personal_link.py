from bot_manager import BotManager
from config import BOT_USERNAME

bot = BotManager()

def generate_personal_link(user_id):
    return f"https://t.me/{BOT_USERNAME}?start={user_id}"