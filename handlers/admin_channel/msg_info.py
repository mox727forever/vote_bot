import aiogram

from classes import ConfigParser


@aiogram.Dispatcher.get_current().channel_post_handler(
    lambda m: m.text == "/msg_info" and m.chat.id == ConfigParser.getint("Bot", "works_channel")
)
async def msg_info(msg: aiogram.types.Message):
    if msg.reply_to_message is None:
        await msg.reply("Работает только в ответ на сообщение")
    else:
        await msg.reply(msg.reply_to_message.as_json())
