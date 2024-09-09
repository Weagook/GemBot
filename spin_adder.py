import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database.models import User
from database.database import AsyncSessionLocal

class DailySpinAdder:
    def __init__(self):
        self.session = AsyncSessionLocal

    async def add_daily_spins(self):
        """
        Добавляет спины всем пользователям в зависимости от их статуса.
        """
        # Количество спинов для каждого статуса
        spins_by_status = {
            "Player": 0,
            "Bronze": 1,
            "Silver": 3,
            "Gold": 5,
            "Platinum": 10
        }

        async with self.session() as session:
            async with session.begin():
                result = await session.execute(select(User))
                users = result.scalars().all()

                for user in users:
                    spins_to_add = spins_by_status.get(user.status, 0)
                    
                    new_spins_count = min((user.spins_count or 0) + spins_to_add, 30)

                    user.spins_count = new_spins_count

                try:
                    await session.commit()
                    print("Спины успешно добавлены всем пользователям.")
                except Exception as e:
                    await session.rollback()
                    print(f"Ошибка при добавлении спинов: {e}")

async def main():
    daily_spin_adder = DailySpinAdder()
    await daily_spin_adder.add_daily_spins()

if __name__ == "__main__":
    asyncio.run(main())