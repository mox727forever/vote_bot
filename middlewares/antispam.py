import aiogram
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled


class ThrottlingMiddleware(BaseMiddleware):
    @staticmethod
    async def on_pre_process_callback_query(call: aiogram.types.CallbackQuery, _):
        try:
            await aiogram.Dispatcher.get_current().throttle("antispam", rate=5)
        except Throttled:
            await call.answer("Антиспам! Подожди 5 секунд, прежде чем проголосовать", show_alert=True)
            raise CancelHandler()


aiogram.Dispatcher.get_current().setup_middleware(ThrottlingMiddleware())
