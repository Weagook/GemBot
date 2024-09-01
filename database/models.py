from sqlalchemy import Column, DateTime, Integer, String
from database.database import Base
from datetime import datetime, timezone

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)                                 # Уникальный ID в БД
    telegram_id = Column(Integer, nullable=False)                                      # ID телеграма
    name = Column(String, index=True, nullable=True)                                   # Имя с телеграма
    tag = Column(String, index=True, nullable=True)                                    # Тег (UTM метка)
    status = Column(String, index=True, default='Player')                              # Статус
    spins_count = Column(Integer, default=30)                                          # Количество спинов
    followers = Column(Integer, default=0)                                             # Количество рефералов
    referral_link = Column(String, index=True)                                         # Реферальная ссылка
    points = Column(Integer, default=0)                                                # Количество очков
    inviter_id = Column(Integer, nullable=True)                                        # ID телеграма пригласившего человека
    registration_date = Column(DateTime, default=datetime.utcnow)                      # Дата регистрации пользователя
