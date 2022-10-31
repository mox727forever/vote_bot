import aiogram

from classes import FSMStatesGroup
from keyboards import get_main_keyboard


@aiogram.Dispatcher.get_current().message_handler(lambda m: m.text == "Помощь 🎃", state=FSMStatesGroup.start)
@aiogram.Dispatcher.get_current().message_handler(commands=["help"], state="*")
async def help_cmd(msg: aiogram.types.Message):
    await FSMStatesGroup.start.set()
    await msg.answer(
        """
<a href="https://t.me/genshix_creators_channel/1182"><b>Условия конкурса и награды описаны в этом посте:</b>
https://t.me/genshix_creators_channel/1182</a>

<b>Процесс голосования:</b>
🔸 Вам даются работы в перемешанном порядке, которые вам нужно оценить
🔸 Вы можете поставить оценку от 1 до 5 (1 - ужасно, 5 - отлично)
🔸 В боте работает антиспам: после каждой оценки необходимо подождать 5 секунд, чтобы оценить следующую работу

❗ Если вы один из участников конкурса, вы не можете голосовать
        """, reply_markup=get_main_keyboard(), parse_mode="HTML", disable_web_page_preview=True
    )
