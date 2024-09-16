from config import IMAGES, ANIMATION
from random import choice, randint

win_message = ''''✅✅✅
# You won! Great job, keep it up!💪'''
lose_message = '''❌❌❌
# Unsuccessful attempt, but no worries, you'll get it next time!'''


async def play_roll(bot, database, user_id, KEYBOARDS, query):
    spins = await database.get_user_property(user_id, 'spins_count')
    print(f'UserID: {user_id}, Spins: {spins}')
    suffix = query.data.split('_')[1]
    roll = [3, 5, 10][randint(1,3)-1]
    if spins < 1:
        message = '''You've played the maximum number of times today. Wait until the next day or invite more friends using your referral link to play more each day'''
        await bot.send_photo(chat_id=user_id, photo=IMAGES['no_spins'], caption=message, reply_markup=KEYBOARDS['lobby'])
        return
    
    await database.remove_spins(user_id, 1)
    if 'x'+str(roll) == suffix:
        await bot.send_animation(chat_id=user_id, animation=ANIMATION['x'+str(roll)], caption=win_message, reply_markup=KEYBOARDS['next_try_keyboard'])
        await database.add_points(user_id, 1)
        await database.add_spins(user_id, 1)
        return

    await bot.send_animation(chat_id=user_id, animation=ANIMATION['x'+str(roll)],caption=lose_message, reply_markup=KEYBOARDS['next_try_keyboard'])
    return