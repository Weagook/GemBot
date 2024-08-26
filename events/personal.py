async def entry_personal(bot, IMAGE_ID, DATABASE, user_id, message, KEYBOARDS):
    referal_link = DATABASE.get_link(user_id)
    cur_message = message.replace('[REFERRAL_LINK]', referal_link)
    await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=cur_message, reply_markup=KEYBOARDS['personal'])