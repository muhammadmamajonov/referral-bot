from cgitb import text
from aiogram import types
from aiogram.dispatcher import FSMContext

from states.change_personal_data_states import ChangePersonalData
from keyboards.default.settings_keyboards import settings_keyboard_en, settings_keyboard_ru, settings_keyboard_uz

from loader import dp, db

# -------------- Yoshni o'zgartirish -------------- #
@dp.message_handler(text="Yoshni o'zgartirish", state=ChangePersonalData.main)
async def change_age_uz(message: types.Message):
    await message.answer(text="Yoshni kiriting")
    await ChangePersonalData.age.set()

@dp.message_handler(text="Изменить возраст", state=ChangePersonalData.main)
async def change_age_ru(message: types.Message):
    await message.answer(text="Введите возраст")
    await ChangePersonalData.age.set()

@dp.message_handler(text="Change age", state=ChangePersonalData.main)
async def change_age_en(message: types.Message):
    await message.answer(text="Enter your age")
    await ChangePersonalData.age.set()


@dp.message_handler(state=ChangePersonalData.age)
async def set_age(message: types.Message):
    db.set_age(id=message.from_user.id, age=message.text)
    language = db.get_language(id=message.from_user.id)
    
    if language == 'en':
        await message.answer(text=f"Age changed. \n current age:{message.text}")
    elif language == 'ru':
        await message.answer(text=f"Возраст изменен. \n текущий возраст:{message.text}")
    else:
        await message.answer(text=f"Yosh o'zgartirildi. \n hozirgi yosh:{message.text}")
    await ChangePersonalData.main.set()


# -------------- Manzilni o'zgartirish -------------- #

@dp.message_handler(text="Manzilni o'zgartirish", state=ChangePersonalData.main)
async def change_address_uz(message: types.Message):
    await message.answer(text="Manzilni kiriting")
    await ChangePersonalData.address.set()

@dp.message_handler(text="Change address", state=ChangePersonalData.main)
async def change_address_en(message: types.Message):
    await message.answer(text="Enter address")
    await ChangePersonalData.address.set()

@dp.message_handler(text="Сменить адрес", state=ChangePersonalData.main)
async def change_address_ru(message: types.Message):
    await message.answer(text="Введите адрес")
    await ChangePersonalData.address.set()


@dp.message_handler(state=ChangePersonalData.address)
async def set_address(message: types.Message):
    db.set_address(id=message.from_user.id, address=message.text)
    language = db.get_language(id=message.from_user.id)
    
    if language == 'en':
        await message.answer(text=f"Address changed. \n current address:{message.text}")
    elif language == 'ru':
        await message.answer(text=f"Адрес изменен. \n текущий адрес:{message.text}")
    else:
        await message.answer(text=f"Manzil o'zgartirildi. \n joriy manzil:{message.text}")
    
    await ChangePersonalData.main.set()

# -------------- Back to settings -------------- #
@dp.message_handler(text="⬅️", state=ChangePersonalData.main)
async def back_to_settings(message: types.Message, state: FSMContext):
    language = db.get_language(id=message.from_user.id)

    if language == 'ru':
        await message.answer(text="⚙️ Настройки", reply_markup=settings_keyboard_ru)
    elif language == 'en':
        await message.answer(text="⚙️ Settings", reply_markup=settings_keyboard_en)
    else:
        await message.answer(text="⚙️ Sozlash", reply_markup=settings_keyboard_uz)
    await state.finish()