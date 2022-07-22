from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.keyboards import language_keyboard
from keyboards.default.settings_keyboards import change_account_number_keyboard_en
from keyboards.default.change_personal_data_keyboards import change_personal_data_keyboard_en
from states.change_account_number_states import ChangeAccount
from states.change_personal_data_states import ChangePersonalData


from loader import dp


@dp.message_handler(text='🌐 Select language')
async def set_language(message: types.Message):
    text = f"""🇺🇿Tilni o'zgartirish uchun kerakli tugma ustiga bosing.
🇬🇧Click the button you want to change the language.
🇷🇺Нажмите кнопку, язык которой вы хотите изменить."""

    await message.answer(text=text, reply_markup=language_keyboard)


@dp.message_handler(text="💳 Change account number")
async def change_account_number(message: types.Message):
    text = f"💳 Change account number"
    await message.answer(text=text, reply_markup=change_account_number_keyboard_en)
    await ChangeAccount.in_change_account.set()


@dp.message_handler(text="👤 Change of personal data")
async def change_personal_data(message: types.Message):
    text = "👤 Change of personal data"
    await message.answer(text=text, reply_markup=change_personal_data_keyboard_en)
    await ChangePersonalData.main.set()



