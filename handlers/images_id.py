from aiogram import Router, F
from aiogram.types import Message

ADMIN_ID = 1373643498

router = Router()

@router.message(F.photo)
async def handle_photo(message: Message):
    user_id = message.from_user.id
    if user_id == ADMIN_ID:
        photo_id = message.photo[-1].file_id 
        await message.answer(f'ID вашей фотографии: {photo_id}')