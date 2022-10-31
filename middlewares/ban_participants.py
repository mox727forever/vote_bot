import aiogram
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from classes.db_connector import DBConnector


class BanParticipants(BaseMiddleware):
    @staticmethod
    async def on_pre_process_message(msg: aiogram.types.Message, _):
        result = await DBConnector.async_sql_request("SELECT count(1) FROM works WHERE user_id = $1", msg.from_user.id)
        if result[0]['count'] > 0:
            await msg.answer("Вы учавствуете в конкурсе, вам запрещено голосовать!")
            raise CancelHandler()

    @staticmethod
    async def on_pre_process_callback_query(call: aiogram.types.CallbackQuery, _):
        result = await DBConnector.async_sql_request("SELECT count(1) FROM works WHERE user_id = $1", call.from_user.id)
        if result[0]['count'] > 0:
            await call.answer("Вы учавствуете в конкурсе, вам запрещено голосовать!", show_alert=True)
            raise CancelHandler()


aiogram.Dispatcher.get_current().setup_middleware(BanParticipants())
