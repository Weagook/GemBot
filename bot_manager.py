from aiogram import Bot
from config import BOT_API_TOKEN

class BotManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = Bot(token=BOT_API_TOKEN)
        return cls._instance