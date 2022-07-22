from aiogram.dispatcher.filters.state import StatesGroup, State


class ChangePersonalData(StatesGroup):
    main = State()
    age = State()
    address = State()
    