import aiogram

from classes import FSMStatesGroup
from keyboards import get_main_keyboard


@aiogram.Dispatcher.get_current().message_handler(lambda m: m.text == "Главное меню 👻", state=FSMStatesGroup.start)
@aiogram.Dispatcher.get_current().message_handler(commands=["start"], state="*")
async def start_cmd(msg: aiogram.types.Message):
    await FSMStatesGroup.start.set()
    await msg.answer("Хей! Время голосовать за лучшую работу! Просто нажми кнопку снизу, чтобы начать "
                     "голосование 😏\n\nЧтобы узнать подробнее о процессе голосования, используй команду /help",
                     reply_markup=get_main_keyboard())
