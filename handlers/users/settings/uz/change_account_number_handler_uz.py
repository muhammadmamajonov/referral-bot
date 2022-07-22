from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.settings_keyboards import settings_keyboard_uz, settings_keyboard_en, settings_keyboard_ru
from states.change_account_number_states import ChangeAccount

from loader import dp, db

# -------------------- Change Click
@dp.message_handler(text="💳 Click raqamini o'zgartirish", state=ChangeAccount.in_change_account)
async def change_click_number(message: types.Message):
   
    text = f"Yangi click raqamini kiriting:"
    await message.answer(text=text)
    await ChangeAccount.in_click.set()

@dp.message_handler(state=ChangeAccount.in_click)
async def set_click_number(message: types.Message):
    db.set_click_number(id=message.from_user.id, click_number=message.text)
    text = f"Click raqam yangilandi. \n yangi raqam: {message.text}"
    await message.answer(text)
    await ChangeAccount.in_change_account.set()


# -------------------- Change Phone
@dp.message_handler(text="📞 Tel nomerni o'zgartirish", state=ChangeAccount.in_change_account)
async def change_phone_number(message: types.Message):
    text = f"Yangi telefon raqamini kiriting:"
    await message.answer(text=text)
    await ChangeAccount.in_phone_number.set()

@dp.message_handler(state=ChangeAccount.in_phone_number)
async def set_phone_number(message: types.Message):
    db.set_phone(id=message.from_user.id, phone=message.text)
    text = f"Telefon raqam yangilandi. \n yangi raqam: {message.text}"
    await message.answer(text)
    await ChangeAccount.in_change_account.set()

# -------------- Back to settings -------------- #
@dp.message_handler(text="⬅️", state=ChangeAccount.in_change_account)
async def back_to_settings(message: types.Message, state: FSMContext):
    language = db.get_language(id=message.from_user.id)

    if language == 'ru':
        await message.answer(text="⚙️ Настройки", reply_markup=settings_keyboard_ru)
    elif language == 'en':
        await message.answer(text="⚙️ Settings", reply_markup=settings_keyboard_en)
    else:
        await message.answer(text="⚙️ Sozlash", reply_markup=settings_keyboard_uz)
    await state.finish()