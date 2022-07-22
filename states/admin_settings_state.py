from aiogram.dispatcher.filters.state import StatesGroup, State


class SettingsState(StatesGroup):
    change_contact = State()
    change_price = State()
    
    