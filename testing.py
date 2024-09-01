import asyncio
from database.async_database import AsyncDatabase

db = AsyncDatabase()

async def main():
    followers = await db.get_user_property(848371439, 'followers')
    print(followers)



if __name__ == '__main__':
    asyncio.run(main())