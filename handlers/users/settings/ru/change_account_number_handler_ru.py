from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.settings_keyboards import settings_keyboard_ru
from states.change_account_number_states import ChangeAccount

from loader import dp, db

# -------------------- Change Click
@dp.message_handler(text="💳 Изменить номер Click", state=ChangeAccount.in_change_account)
async def change_click_number(message: types.Message):
    
    text = f"Введите новый номер Click:"
    await message.answer(text=text)
    await ChangeAccount.in_click.set()

@dp.message_handler(state=ChangeAccount.in_click)
async def set_click_number(message: types.Message):
    db.set_click_number(id=message.from_user.id, click_number=message.text)
    text = f"Обновлен номер Click. \n новый номер: {message.text}"
    await message.answer(text)
    await ChangeAccount.in_change_account.set()


# -------------------- Change Phone
@dp.message_handler(text="📞 Изменить номер телефона", state=ChangeAccount.in_change_account)
async def change_phone_number(message: types.Message):
    text = f"Введите новый номер телефона:"
    await message.answer(text=text)
    await ChangeAccount.in_phone_number.set()

@dp.message_handler(state=ChangeAccount.in_phone_number)
async def set_phone_number(message: types.Message):
    db.set_phone(id=message.from_user.id, phone=message.text)
    text = f"Номер телефона обновлен. \n новый номер: {message.text}"
    await message.answer(text)
    await ChangeAccount.in_change_account.set()

