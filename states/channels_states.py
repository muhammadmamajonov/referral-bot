from aiogram.dispatcher.filters.state import StatesGroup, State

class ChannelStates(StatesGroup):
    channels = State()
    add_new = State()
    id = State()
    link = State()
    delete = State()
