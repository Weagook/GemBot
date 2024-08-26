from config import PLAY_IMAGES
from random import choice


async def play_roll(bot, DATABASE, user_id, KEYBOARDS, query):
    spins = DATABASE.get_spins(user_id)
    if spins < 1:
        message = '''You've played the maximum number of times today. Wait until the next day or invite more friends using your referral link to play more each day'''
        await bot.send_message(chat_id=user_id, text=message, reply_markup=KEYBOARDS['lobby'])
        return
    
    random_key = choice(list(PLAY_IMAGES.keys()))
    IMAGE_ID = PLAY_IMAGES[random_key]
    if random_key.split('_')[0] == 'win':
        message = '''✅✅✅
You won! Great job, keep it up!💪'''
        points = int(query.data.split('_')[1][1:])
        DATABASE.add_points(user_id, points)
    else:
        message = '''❌❌❌
Unsuccessful attempt, but no worries, you'll get it next time!'''
    DATABASE.remove_spin(user_id)
    await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=message, reply_markup=KEYBOARDS['play'])