from aiogram.dispatcher.filters.state import StatesGroup, State


class ChangeAccount(StatesGroup):
    in_change_account = State()
    in_click = State()
    in_phone_number = State()