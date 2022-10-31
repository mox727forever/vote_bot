import aiogram.types


def get_main_keyboard():
    keyboard = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(aiogram.types.KeyboardButton("Главное меню 👻"), aiogram.types.KeyboardButton("Помощь 🎃"))
    keyboard.add(aiogram.types.KeyboardButton("Начать голосование ☠"))
    return keyboard
