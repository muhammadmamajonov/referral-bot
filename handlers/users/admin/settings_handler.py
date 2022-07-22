from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.admin.admin_settings_keyboard import admin_settings_menu_keyboard
from keyboards.default.admin.admin_main_menu_keyboard import admin_main_menu
from states.admin_settings_state import SettingsState
from loader import dp, db


@dp.message_handler(text="⚙️ Sozlamalar")
async def settings(message: types.Message):
    await message.answer("⚙️ Sozlamalar", reply_markup=admin_settings_menu_keyboard)

@dp.message_handler(text="📞 Bog'lanish uchun raqamni o'zgartirish")
async def change_contact_number(message: types.Message):
    await SettingsState.change_contact.set()
    await message.answer("Telefon raqmini kiriting:")

@dp.message_handler(state=SettingsState.change_contact)
async def get_new_phone_num(message: types.Message, state: FSMContext):
    db.set_contact_number(phone_number=message.text)
    await state.finish()
    await message.answer(f"Telefon raqam o'zgartirildi: \n joriy raqam: {message.text}")


@dp.message_handler(text="💸 Taklif uchun narxni belgilash")
async def set_invation_price(message: types.Message):
    await SettingsState.change_price.set()
    await message.answer("Yangi narxni kiriting \n ❗️ Barcha hisoblar O'zbekiston so'mida \n Faqat raqam kiriting")

@dp.message_handler(state=SettingsState.change_price)
async def get_new_price(message: types.Message, state: FSMContext):
    db.set_price_for_invited(price=message.text)
    await state.finish()
    await message.answer(f"Yangi narx belgilandi: \n joriy narx: {message.text} so'm")


@dp.message_handler(text='◀️ Ortga')
async def back(message: types.Message):
    await message.answer("Bosh menyu", reply_markup=admin_main_menu)