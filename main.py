import urllib.parse

import aiogram
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from classes.cfgparser import ConfigParser
import middlewares
import handlers

bot = aiogram.Bot(ConfigParser.get("Bot", "token"))
aiogram.Bot.set_current(bot)

redis_cnct = urllib.parse.urlparse(ConfigParser.get("Redis", "url"))
fsm_storage = RedisStorage2(host=redis_cnct.hostname, port=redis_cnct.port,
                            password=redis_cnct.password, pool_size=1000)
dp = aiogram.Dispatcher(bot, storage=fsm_storage)
aiogram.Dispatcher.set_current(dp)

handlers.init()
middlewares.init()

aiogram.executor.start_polling(dp, skip_updates=True)
