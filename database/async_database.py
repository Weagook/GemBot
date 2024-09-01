from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from database.models import User
from database.database import AsyncSessionLocal

class AsyncDatabase:
    def __init__(self):
        self.session = AsyncSessionLocal

    async def add_user(
        self, 
        telegram_id: int, 
        name: str = None, 
        tag: str = None, 
        refferal_link: str = None, 
        inviter_id: str = None
    ) -> bool:
        """
        Добавляет нового пользователя в базу данных.
        
        :param telegram_id: ID пользователя в Telegram
        :param name: Имя пользователя (по умолчанию None)
        :param tag: Дополнительная метка пользователя (по умолчанию None)
        :param refferal_link: Реферальная ссылка (по умолчанию None)
        :param inviter_id: ID пригласившего пользователя (по умолчанию None)
        :return: True, если пользователь успешно добавлен, False, если пользователь уже существует
        """

        if inviter_id is not None and inviter_id == telegram_id:
            # Нельзя добавить самого себя в качестве реферала
            return False

        async with self.session() as session:
            async with session.begin():
                # Проверка наличия пользователя с таким telegram_id
                result = await session.execute(select(User).filter_by(telegram_id=telegram_id))
                user = result.scalars().first()

                if user:
                    # Пользователь уже существует
                    return False

                # Создаем нового пользователя
                new_user = User(
                    telegram_id=telegram_id,
                    name=name,
                    tag=tag,
                    referral_link=refferal_link,
                    inviter_id=inviter_id
                )
                session.add(new_user)
                try:
                    await session.commit()

                    # Если указан inviter_id, обновляем список followers у пригласившего
                    if inviter_id:
                        print('Отработало условие "if inviter"')
                        await self.add_follower(inviter_id, telegram_id)

                    return True
                except IntegrityError:
                    # Если возникает ошибка целостности (например, уникальное ограничение),
                    # возвращаем False
                    await session.rollback()
                    return False
                
    async def add_follower(self, inviter_id: int, follower_id: int) -> bool:
        """
        Увеличивает количество рефералов для пользователя с указанным inviter_id.

        :param inviter_id: ID пригласившего пользователя в Telegram
        :param follower_id: ID нового подписчика в Telegram
        :return: True, если обновление прошло успешно, иначе False
        """

        if inviter_id == follower_id:
            # Нельзя добавить самого себя в качестве реферала
            return False
        
        if inviter_id:
            inviter_id = int(inviter_id)
        if follower_id:
            follower_id = int(follower_id)
        async with self.session() as session:
            async with session.begin():
                result = await session.execute(select(User).filter_by(telegram_id=int(inviter_id)))
                inviter = result.scalars().first()

                if inviter:
                    inviter.followers += 1
                    try:
                        await session.commit()
                        return True
                    except IntegrityError:
                        await session.rollback()
                        return False

                return False

    async def user_exists(self, telegram_id: int) -> bool:
        """
        Проверяет, существует ли пользователь с указанным telegram_id.
        
        :param telegram_id: ID пользователя в Telegram
        :return: True, если пользователь существует, иначе False
        """
        async with self.session() as session:
            async with session.begin():
                result = await session.execute(select(User).filter_by(telegram_id=telegram_id))
                user = result.scalars().first()
                return user is not None

    async def get_user_property(self, telegram_id: int, property_name: str):
        """
        Возвращает указанное свойство пользователя по telegram_id.

        :param telegram_id: ID пользователя в Telegram
        :param property_name: Имя свойства, которое необходимо получить
        :return: Значение свойства или None, если пользователь не найден
        """
        async with self.session() as session:
            async with session.begin():
                result = await session.execute(select(User).filter_by(telegram_id=telegram_id))
                user = result.scalars().first()

                if user and hasattr(user, property_name):
                    return getattr(user, property_name)
                return None

    async def get_user_by_telegram_id(self, telegram_id: int) -> dict:
        """
        Возвращает полную запись пользователя по telegram_id.

        :param telegram_id: ID пользователя в Telegram
        :return: Словарь с данными пользователя или None, если пользователь не найден
        """
        async with self.session() as session:
            async with session.begin():
                result = await session.execute(select(User).filter_by(telegram_id=telegram_id))
                user = result.scalars().first()

                if user:
                    return {
                        "id": user.id,
                        "telegram_id": user.telegram_id,
                        "name": user.name,
                        "tag": user.tag,
                        "status": user.status,
                        "spins_count": user.spins_count,
                        "followers": user.followers,
                        "referral_link": user.referral_link,
                        "points": user.points,
                        "inviter_id": user.inviter_id
                    }
                return None
            

    async def update_user_name(self, telegram_id: int, new_name: str) -> bool:
        """
        Обновляет имя пользователя по указанному telegram_id.

        :param telegram_id: ID пользователя в Telegram
        :param new_name: Новое имя пользователя
        :return: True, если имя успешно обновлено, иначе False
        """
        async with self.session() as session:
            async with session.begin():
                # Найти пользователя по telegram_id
                result = await session.execute(select(User).filter_by(telegram_id=telegram_id))
                user = result.scalars().first()

                if user:
                    # Обновить имя пользователя
                    user.name = new_name
                    try:
                        await session.commit()
                        return True
                    except IntegrityError:
                        # Если возникает ошибка целостности, вернуть False
                        await session.rollback()
                        return False
                return False


    async def get_all_users(self) -> dict:
        """
        Возвращает всех пользователей с их именами и количеством очков.

        :return: Словарь, где ключ - telegram_id, а значение - словарь с именем и количеством очков пользователя
        """
        async with self.session() as session:
            async with session.begin():
                # Выполняем запрос на выборку всех пользователей
                result = await session.execute(select(User))
                users = result.scalars().all()

                # Создаем словарь с необходимыми данными
                user_data = {
                    user.telegram_id: {
                        'name': user.name or 'Unknown',
                        'points': user.points or 0
                    }
                    for user in users
                }
                return user_data
            
    async def add_points(self, telegram_id: int, points: int) -> bool:
        """
        Добавляет указанное количество очков пользователю по telegram_id.

        :param telegram_id: ID пользователя в Telegram
        :param points: Количество очков для добавления
        :return: True, если очки успешно добавлены, иначе False
        """
        async with self.session() as session:
            async with session.begin():
                result = await session.execute(select(User).filter_by(telegram_id=telegram_id))
                user = result.scalars().first()

                if user:
                    user.points = (user.points or 0) + points
                    try:
                        await session.commit()
                        return True
                    except IntegrityError:
                        await session.rollback()
                        return False
                return False

    async def add_spins(self, telegram_id: int, spins: int) -> bool:
        """
        Добавляет указанное количество спинов пользователю по telegram_id.

        :param telegram_id: ID пользователя в Telegram
        :param spins: Количество спинов для добавления
        :return: True, если спины успешно добавлены, иначе False
        """
        async with self.session() as session:
            async with session.begin():
                result = await session.execute(select(User).filter_by(telegram_id=telegram_id))
                user = result.scalars().first()

                if user:
                    user.spins_count = (user.spins_count or 0) + spins
                    try:
                        await session.commit()
                        return True
                    except IntegrityError:
                        await session.rollback()
                        return False
                return False

    async def remove_spins(self, telegram_id: int, spins: int) -> bool:
        """
        Удаляет указанное количество спинов у пользователя по telegram_id.

        :param telegram_id: ID пользователя в Telegram
        :param spins: Количество спинов для удаления
        :return: True, если спины успешно удалены, иначе False
        """
        async with self.session() as session:
            async with session.begin():
                result = await session.execute(select(User).filter_by(telegram_id=telegram_id))
                user = result.scalars().first()

                if user and (user.spins_count or 0) >= spins:
                    user.spins_count -= spins
                    try:
                        await session.commit()
                        return True
                    except IntegrityError:
                        await session.rollback()
                        return False
                return False
    
    
    async def get_followers(self, telegram_id: int) -> list:
        """
        Возвращает список пользователей, у которых указанный telegram_id является inviter_id.

        :param telegram_id: ID пользователя в Telegram, который является inviter_id
        :return: Список словарей с данными пользователей, у которых этот telegram_id указан как inviter_id
        """
        async with self.session() as session:
            async with session.begin():
                # Выполняем запрос на выборку пользователей, у которых inviter_id соответствует указанному telegram_id
                result = await session.execute(select(User).filter_by(inviter_id=telegram_id))
                users = result.scalars().all()

                # Создаем список словарей с необходимыми данными пользователей
                followers = [
                    {
                        "id": user.id,
                        "telegram_id": user.telegram_id,
                        "name": user.name,
                        "tag": user.tag,
                        "status": user.status,
                        "spins_count": user.spins_count,
                        "followers": user.followers,
                        "referral_link": user.referral_link,
                        "points": user.points,
                        "inviter_id": user.inviter_id
                    }
                    for user in users
                ]
                return followers