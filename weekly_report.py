import asyncio
import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database.models import User
from database.database import AsyncSessionLocal
from aiogram import Bot
from aiogram.types import FSInputFile
from config import BOT_API_TOKEN, ADMIN_ID
import os


class WeeklyReport:
    def __init__(self):
        self.session = AsyncSessionLocal
        self.bot = Bot(token=BOT_API_TOKEN)

    async def generate_csv(self):
        """
        Генерирует CSV-файл с данными всех пользователей и сохраняет его на диск.
        """
        async with self.session() as session:
            async with session.begin():
                # Выбираем всех пользователей
                result = await session.execute(select(User))
                users = result.scalars().all()

                # Создаем DataFrame
                data = [{
                    'ID': user.id,
                    'Telegram ID': user.telegram_id,
                    'Name': user.name,
                    'Tag': user.tag,
                    'Status': user.status,
                    'Spins Count': user.spins_count,
                    'Followers': user.followers,
                    'Referral Link': user.referral_link,
                    'Points': user.points,
                    'Inviter ID': user.inviter_id
                } for user in users]

                df = pd.DataFrame(data)

                # Сохраняем DataFrame в CSV-файл
                file_path = 'user_report.csv'
                df.to_csv(file_path, index=False, encoding='utf-8')
                return file_path
            
    async def reset_points(self):
        """
        Сбрасывает points у всех пользователей.
        """
        async with self.session() as session:
            async with session.begin():
                await session.execute(update(User).values(points=0))
                await session.commit()

    async def send_report(self):
        """
        Отправляет отчет в виде CSV-файла админу через бота.
        """
        # Генерируем и сохраняем CSV-файл
        csv_file_path = await self.generate_csv()

        # Отправляем файл админу
        csv_file = FSInputFile(csv_file_path, filename="user_report.csv")
        await self.bot.send_document(
            chat_id=ADMIN_ID,
            document=csv_file,
            caption="Weekly User Report"
        )

        # Удаляем файл после отправки
        if os.path.exists(csv_file_path):
            os.remove(csv_file_path)

        # Сбрасываем points у всех пользователей
        await self.reset_points()


async def main():
    weekly_report = WeeklyReport()
    await weekly_report.send_report()

if __name__ == "__main__":
    asyncio.run(main())
