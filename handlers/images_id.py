from aiogram import Router, F
from aiogram.types import Message
from config import ADMIN_ID

router = Router()

@router.message(F.photo)
async def handle_photo(message: Message):
    user_id = message.from_user.id
    if user_id == ADMIN_ID:
        photo_id = message.photo[-1].file_id 
        await message.answer(f'ID вашей фотографии: {photo_id}')

@router.message(F.video)
async def handle_video(message: Message):
    user_id = message.from_user.id
    if user_id == ADMIN_ID:
        video_id = message.video.file_id
        await message.answer(f'ID вашего видео: {video_id}')

@router.message(F.animation)
async def handle_gif(message: Message):
    user_id = message.from_user.id
    if user_id == ADMIN_ID:
        gif_id = message.animation.file_id
        await message.answer(f'ID вашей GIF: {gif_id}')