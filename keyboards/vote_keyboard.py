import aiogram


def get_vote_keyboard(work_id: int):
    keyboard = aiogram.types.InlineKeyboardMarkup()
    keyboard.add(*[
        aiogram.types.InlineKeyboardButton(i, callback_data=f"vote.{work_id}.{i}") for i in range(1, 6)
    ])
    return keyboard
