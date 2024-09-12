from config import VIDEO, ANIMATION

async def entry_choice_play(bot, user_id, KEYBOARDS):
    message = '''What does your intuition tell you? How high will the plane fly?
No doubt, luck will be on your side!'''
    await bot.send_animation(chat_id=user_id, animation=ANIMATION['next_try'], caption=message, reply_markup=KEYBOARDS['play'])