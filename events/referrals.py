async def entry_referrals(bot, database, user_id, message, KEYBOARDS):
    count_ref = await database.get_user_property(user_id, 'followers')
    if count_ref < 1:
        answer = "You don't have any referrals yet"
    elif count_ref == 1:
        answer = 'You have 1 referral'
    else:
        answer = f'You have {count_ref} referrals'
    cur_message = message.replace('[PLACEHOLDER]', answer)
    await bot.send_message(chat_id=user_id, text=cur_message, reply_markup=KEYBOARDS['personal'])