from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMStatesGroup(StatesGroup):
    start = State()
    vote_start = State()
