from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.keyboards import edit_rules_keyboard
from states.change_rules_state import ChangeRules
from loader import dp, db


@dp.message_handler(text='🔔 Qoidalarni sozlash')
async def setting_rules(message: types.Message):
    rules = db.get_rules()

    rules_txt = f"""
{rules[1]}
------------------------
{rules[2]}
------------------------
{rules[3]}
"""

    await message.answer(text=rules_txt, reply_markup=edit_rules_keyboard)


@dp.callback_query_handler(text='change_rules_uz')
async def set_state_change_rules_uz(call: types.CallbackQuery):
    await ChangeRules.change_uz.set()
    await call.message.answer("Yangi qoidalarni kiriting!")

@dp.message_handler(state=ChangeRules.change_uz)
async def change_rules_uz(message: types.Message, state: FSMContext):
    db.set_rules_uz(rules_uz=message.text)
    await message.answer("✅ o'zgartirildi")
    await state.finish()


@dp.callback_query_handler(text='change_rules_en')
async def set_state_change_rules_en(call: types.CallbackQuery):
    await ChangeRules.change_en.set()
    await call.message.answer("Enter new rules!")

@dp.message_handler(state=ChangeRules.change_en)
async def change_rules_en(message: types.Message, state: FSMContext):
    print(message.text)
    db.set_rules_en(rules_en=message.text)
    await message.answer("✅ changed")
    await state.finish()


@dp.callback_query_handler(text='change_rules_ru')
async def set_state_change_rules_ru(call: types.CallbackQuery):
    await ChangeRules.change_ru.set()
    await call.message.answer("Введите новые правила!")

@dp.message_handler(state=ChangeRules.change_ru)
async def change_rules_ru(message: types.Message, state: FSMContext):
    db.set_rules_ru(rules_ru=message.text)
    await message.answer("✅ измененный")
    await state.finish()