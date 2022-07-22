from pydoc import cli
from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.settings_keyboards import settings_keyboard_en, settings_keyboard_ru, settings_keyboard_uz
from states.change_account_number_states import ChangeAccount

from loader import dp, db

# -------------------- Change Click
@dp.message_handler(text="💳 Change the Click number", state=ChangeAccount.in_change_account)
async def change_click_number(message: types.Message):
    text = f"Enter a new Click number:"
    await message.answer(text=text)
    await ChangeAccount.in_click.set()

@dp.message_handler(state=ChangeAccount.in_click)
async def set_click_number(message: types.Message):
    db.set_click_number(id=message.from_user.id, click_number=message.text)
    text = f"Click number updated. \n new number: {message.text}"
    await message.answer(text)
    await ChangeAccount.in_change_account.set()


# -------------------- Change Phone
@dp.message_handler(text="📞 Change the phone number", state=ChangeAccount.in_change_account)
async def change_phone_number(message: types.Message):
    text = f"Enter a new phone number:"
    await message.answer(text=text)
    await ChangeAccount.in_phone_number.set()

@dp.message_handler(state=ChangeAccount.in_phone_number)
async def set_phone_number(message: types.Message):
    db.set_phone(id=message.from_user.id, phone=message.text)
    text = f"Phone number updated. \n new number: {message.text}"
    await message.answer(text)
    await ChangeAccount.in_change_account.set()

