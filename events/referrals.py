async def entry_referrals(bot, IMAGE_ID, DATABASE, user_id, message, KEYBOARDS):
    count_ref = DATABASE.count_followers(user_id)
    if count_ref < 1:
        answer = "You don't have any referrals yet"
    elif count_ref == 1:
        answer = 'You have 1 referral'
    else:
        answer = f'You have {count_ref} referrals'
    cur_message = message.replace('[PLACEHOLDER]', answer)
    await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=cur_message, reply_markup=KEYBOARDS['personal'])