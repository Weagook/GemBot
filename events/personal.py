async def entry_personal(bot, database, user_id, message, KEYBOARDS):
    referal_link = await database.get_user_property(user_id, 'referral_link')
    cur_message = message.replace('[REFERRAL_LINK]', referal_link)
    await bot.send_message(chat_id=user_id, text=cur_message, reply_markup=KEYBOARDS['personal'], disable_web_page_preview=True)