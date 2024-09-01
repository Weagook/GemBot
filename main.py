from aiogram import Bot, Dispatcher
import asyncio
from handlers import setup_routers
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_API_TOKEN
from bot_manager import BotManager
from database.init_db import init_db

async def main():
    await init_db()
    bot = BotManager()
    
    dp = Dispatcher(storage=MemoryStorage())

    setup_routers(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())