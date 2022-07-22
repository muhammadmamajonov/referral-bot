import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from keyboards.inline.keyboards import language_keyboard
from keyboards.default.admin.admin_main_menu_keyboard import admin_main_menu
from keyboards.default.main_manu_keyboards import main_menu_keyboard_en, main_menu_keyboard_ru, main_menu_keyboard_uz
from states.registration_states import Registration
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    referer_id = None
    start_command = message.text.split(' ')
    
    if len(start_command) > 1:
        referer_id = start_command[1]
    
    try:
        if referer_id is not None and referer_id != message.from_user.id:
            db.add_user(id=message.from_user.id, suggested=referer_id, username=message.from_user.username)
            
        else:
            db.add_user(id=message.from_user.id, username=message.from_user.username)
    except sqlite3.IntegrityError as err:
        pass
    
    if f"{message.from_user.id}" in ADMINS:
        await message.answer(f"Salom Admin, botga xush kelibsiz!", reply_markup=admin_main_menu)
    else:
        if db.select_user(message.from_user.id) is not None:
            language = db.get_language(message.from_user.id)
            if language == 'en':
                await message.answer("You have restarted the bot, you can take full advantage of all updates", reply_markup=main_menu_keyboard_en)
            elif language == 'ru':
                await message.answer("Вы перезапустили бота, можете в полной мере воспользоваться всеми обновлениями", reply_markup=main_menu_keyboard_ru)
            else:
                await message.answer("Botni qaytadan ishga tushurdingiz, Barcha yangilanishlardan to'liq foydalanihsingiz mumkin", reply_markup=main_menu_keyboard_uz)
        else:
            text = "Davom etish uchun tilni tanlang.\n"
            text += "Select a language to continue.\n"
            text += "Выберите язык, чтобы продолжить"

            await message.answer(f"Salom, {message.from_user.full_name}!")
            await message.answer(text=text, reply_markup=language_keyboard)
            await Registration.language_seletction.set()