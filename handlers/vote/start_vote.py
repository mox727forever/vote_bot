import aiogram
from aiogram.dispatcher import FSMContext

from classes import FSMStatesGroup
from keyboards import get_confirm_start_keyboard


@aiogram.Dispatcher.get_current().message_handler(
    lambda m: m.text == "Начать голосование ☠", state=FSMStatesGroup.start
)
async def start_voting(msg: aiogram.types.Message, state: FSMContext):
    await state.set_state(FSMStatesGroup.vote_start)
    await msg.answer(
        """
<b>Начинаем голосование!</b>

<i>Для оценки работы используй кнопки снизу (1 - ужасно, 5 - отлично)</i>
        """, reply_markup=get_confirm_start_keyboard(), parse_mode="HTML"
    )
