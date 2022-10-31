import aiogram.types


def get_confirm_start_keyboard():
    return aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True).add(aiogram.types.KeyboardButton("Поехали 😈"))
