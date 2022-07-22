from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.keyboards import language_keyboard

from loader import dp, db



@dp.callback_query_handler(text='uz')
async def set_lang_uz(callback: types.CallbackQuery):
    db.set_language(id=callback.from_user.id, language=callback.data)
    text = "Til O'zbek tiliga o'zgartirildi \n O'zgarish amal qilishi uchun ⬅️ tugmani bosing"
    await callback.message.answer(text)


@dp.callback_query_handler(text='en')
async def set_lang_en(callback: types.CallbackQuery):
    db.set_language(id=callback.from_user.id, language=callback.data)
    text = "The language has been changed to English \n Press the ⬅️ button for the change to take effect"
    await callback.message.answer(text)


@dp.callback_query_handler(text='ru')
async def set_lang_uz(callback: types.CallbackQuery):
    db.set_language(id=callback.from_user.id, language=callback.data)
    text = "Язык изменен на русский \n Нажмите кнопку ⬅️, чтобы изменения вступили в силу."
    await callback.message.answer(text)