from aiogram.dispatcher.filters.state import StatesGroup, State


class WithdrawMoney(StatesGroup):
    in_withdraw = State()