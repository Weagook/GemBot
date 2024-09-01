async def entry_payout_info(bot, IMAGE_ID, database, user_id, message, KEYBOARDS):
    all_user_data = await database.get_user_by_telegram_id(user_id)
    username = all_user_data['name']
    spins = all_user_data['spins_count']
    status = all_user_data['status']
    points = all_user_data['points']
    
    compl_message = message.replace('[NAME]', username).replace('[SPINS]', str(spins)).replace('[STATUS]', status).replace('[POINTS]', str(points))
    await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=compl_message, reply_markup=KEYBOARDS['lobby'])