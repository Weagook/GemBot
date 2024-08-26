async def entry_lobby(bot, IMAGE_ID, DATABASE, user_id, message, KEYBOARDS):
    username = DATABASE.TEMP_DATABASE[user_id]['name']
    spins = DATABASE.TEMP_DATABASE[user_id]['spins']
    status = DATABASE.TEMP_DATABASE[user_id]['status']
    points = DATABASE.get_points(user_id)
    compl_message = message.replace('[NAME]', username).replace('[SPINS]', str(spins)).replace('[STATUS]', status).replace('[POINTS]', str(points))
    await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=compl_message, reply_markup=KEYBOARDS['lobby'])