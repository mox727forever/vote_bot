import aiogram
from aiogram.dispatcher import FSMContext

from classes import FSMStatesGroup
from classes.db_objects.works import Work
from keyboards import get_main_keyboard
from keyboards.vote_keyboard import get_vote_keyboard


@aiogram.Dispatcher.get_current().message_handler(
    lambda m: m.text == "Поехали 😈", state=FSMStatesGroup.vote_start
)
async def voting_handler(msg: aiogram.types.Message, state: FSMContext):
    work = await Work.get_work_for_vote(msg.from_user.id)
    if work is None:
        await state.set_state(FSMStatesGroup.start)
        await msg.answer("Вы уже проголосовали за все работы!", reply_markup=get_main_keyboard())
    else:
        await state.set_state(FSMStatesGroup.vote_start)
        await msg.answer_photo(
            work.file_id,
            """
<b>👆 Оцени работу выше 👆</b>

<i>Для оценки работы используй кнопки снизу (1 - ужасно, 5 - отлично)</i>
            """, reply_markup=get_vote_keyboard(work.work_id), parse_mode="HTML"
        )


@aiogram.Dispatcher.get_current().callback_query_handler(
    lambda c: c.data.startswith("vote."), state=FSMStatesGroup.vote_start
)
async def edit_work(call: aiogram.types.CallbackQuery, state: FSMContext):
    cmd = call.data.split(".")
    voted_work = await Work.get_by_id(int(cmd[1]))
    await voted_work.vote(call.from_user.id, int(cmd[2]))

    await call.message.delete()
    work = await Work.get_work_for_vote(call.from_user.id)
    if work is None:
        await state.set_state(FSMStatesGroup.start)
        await call.message.answer("Вы проголосовали за все работы!", reply_markup=get_main_keyboard())
    else:
        await call.message.answer_photo(
            work.file_id,
            """
    <b>👆 Оцени работу выше 👆</b>
    
    <i>Для оценки работы используй кнопки снизу (1 - ужасно, 5 - отлично)</i>
            """, reply_markup=get_vote_keyboard(work.work_id), parse_mode="HTML"
        )
