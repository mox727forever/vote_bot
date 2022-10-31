from typing import List

import asyncpg

from classes.cfgparser import ConfigParser


class DBConnector:
    pool: asyncpg.Pool = None

    @staticmethod
    async def async_sql_request(request: str, *args) -> List[asyncpg.Record]:
        if DBConnector.pool is None:
            DBConnector.pool = await asyncpg.create_pool(ConfigParser.get("PostgreSQL", "url"))

        async with DBConnector.pool.acquire() as connection:
            try:
                result = await connection.fetch(request, *args)
                await connection.close()
            except Exception as ex:
                await connection.execute("rollback")
                await connection.close()
                raise ex

        return result
