import asyncio
from database.database import engine, Base

async def init_db():
    """
    Создает все таблицы в базе данных, если они еще не созданы.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
