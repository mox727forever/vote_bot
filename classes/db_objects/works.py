import random

from classes.db_connector import DBConnector


class Work:
    def __init__(self, work_id: int, user_id: int, file_id: str):
        self.work_id = work_id
        self.user_id = user_id
        self.file_id = file_id

    async def save(self):
        if self.work_id is None:
            work_id = await DBConnector.async_sql_request(
                "INSERT INTO works (user_id, file_id) VALUES ($1, $2) RETURNING id", self.user_id, self.file_id
            )
            self.work_id = work_id[0]['id']
        else:
            await DBConnector.async_sql_request(
                "UPDATE works SET file_id = $1 WHERE id = $2", self.file_id, self.work_id
            )

    async def vote(self, user_id: int, grade: int):
        if (await DBConnector.async_sql_request(
                "SELECT count(1) FROM votes WHERE user_id = $1 AND work_id = $2", user_id, self.work_id
        ))[0]['count'] != 0:
            raise AttributeError("Already voted")

        await DBConnector.async_sql_request(
            "INSERT INTO votes (user_id, work_id, grade) VALUES ($1, $2, $3)",
            user_id, self.work_id, grade
        )

    @staticmethod
    async def get_work_for_vote(user_id: int):
        result = await DBConnector.async_sql_request(
            "SELECT * FROM works WHERE NOT EXISTS "
            "(SELECT id FROM votes WHERE works.id = votes.work_id AND user_id = $1);", user_id
        )
        if len(result) == 0:
            return None
        chosen_work = random.choice(result)
        return Work(
            work_id=chosen_work['id'],
            user_id=chosen_work['user_id'],
            file_id=chosen_work['file_id']
        )

    @staticmethod
    async def add_work(user_id: int, file_id: str):
        work = Work(work_id=None, user_id=user_id, file_id=file_id)
        await work.save()
        return work

    @staticmethod
    async def get_by_id(work_id: int):
        result = (await DBConnector.async_sql_request("SELECT * FROM works WHERE id = $1", work_id))[0]
        return Work(
            work_id=result['id'],
            user_id=result['user_id'],
            file_id=result['file_id']
        )
