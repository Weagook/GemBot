from utils import get_leaderboard

async def entry_leaderboard(bot, IMAGE_ID, DATABASE, user_id, KEYBOARDS):
    message = get_leaderboard(DATABASE)
    await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=message, reply_markup=KEYBOARDS['personal'])