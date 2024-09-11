from config import VIDEO

async def entry_choice_play(bot, user_id, KEYBOARDS):
    message = '''What does your intuition tell you? How high will the plane fly?
No doubt, luck will be on your side!'''
    await bot.send_video(chat_id=user_id, video=VIDEO['play_video'], caption=message, reply_markup=KEYBOARDS['play'])