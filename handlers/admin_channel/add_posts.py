import aiogram

from classes import ConfigParser
from classes.db_objects.works import Work


@aiogram.Dispatcher.get_current().channel_post_handler(
    lambda m: m.is_forward() and m.chat.id == ConfigParser.getint("Bot", "works_channel"),
    content_types=aiogram.types.ContentType.PHOTO
)
async def save_work_photo(msg: aiogram.types.Message):
    if msg.forward_from is None:
        await msg.reply(f"#неудача\nНе найден пользьзователь {msg.forward_sender_name}")
        return
    await Work.add_work(msg.forward_from.id, msg.photo[-1].file_id)
    await msg.reply("#удача\nДобавлено")


@aiogram.Dispatcher.get_current().channel_post_handler(
    lambda m: m.is_forward() and m.chat.id == ConfigParser.getint("Bot", "works_channel"),
    content_types=aiogram.types.ContentType.DOCUMENT
)
async def save_work_document(msg: aiogram.types.Message):
    if msg.forward_from is None:
        await msg.reply(f"#неудача\nНе найден пользьзователь {msg.forward_sender_name}")
        return

    filename = f"temp/{msg.document.file_name}"
    await msg.document.download(filename)
    temp_photo = await msg.answer_photo(aiogram.types.InputFile(filename))
    await temp_photo.delete()

    await Work.add_work(msg.forward_from.id, temp_photo.photo[-1].file_id)
    await msg.reply("#удача\nДобавлено")
