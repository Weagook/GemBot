from config import IMAGES
from random import choice, randint

win_message = ''''✅✅✅
# You won! Great job, keep it up!💪'''
lose_message = '''❌❌❌
# Unsuccessful attempt, but no worries, you'll get it next time!'''


async def play_roll(bot, database, user_id, KEYBOARDS, query):
    spins = await database.get_user_property(user_id, 'spins_count')
    roll = int(query.data.split('_')[1][1:])
    if spins < roll:
        message = '''You've played the maximum number of times today. Wait until the next day or invite more friends using your referral link to play more each day'''
        await bot.send_photo(chat_id=user_id, photo=IMAGES['no_spins'], caption=message, reply_markup=KEYBOARDS['lobby'])
        return
    
    random_number = randint(1, 2)
    await database.remove_spins(user_id, roll)
    if random_number == 1:
        await bot.send_photo(chat_id=user_id, photo=IMAGES['win'], caption=win_message, reply_markup=KEYBOARDS['play'])
        await database.add_points(user_id, roll)
        return
    if random_number == 2:
        await bot.send_message(chat_id=user_id, text=lose_message, reply_markup=KEYBOARDS['play'])
        return