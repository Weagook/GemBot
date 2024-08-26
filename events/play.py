async def entry_choice_play(bot, DATABASE, user_id, IMAGE_ID, KEYBOARDS):
    message = '''What does your intuition tell you? How high will the plane fly?
No doubt, luck will be on your side!'''
    await bot.send_photo(chat_id=user_id, photo=IMAGE_ID, caption=message, reply_markup=KEYBOARDS['play'])