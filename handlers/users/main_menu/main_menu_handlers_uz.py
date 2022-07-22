from aiogram import types
from keyboards.default.settings_keyboards import  settings_keyboard_uz
from keyboards.default.make_money_keyboards import make_money_menu_keyboard_uz
from keyboards.default.main_manu_keyboards import main_menu_keyboard_uz, main_menu_keyboard_en, main_menu_keyboard_ru
from keyboards.default.balans_keyboards import balans_keyboard_uz
from loader import dp, db


@dp.message_handler(text='🤑 Pul ishlash')
async def make_money(message: types.Message):
    await message.answer("Pul ishlash 🤑 ", reply_markup=make_money_menu_keyboard_uz)


@dp.message_handler(text='Balans 🤑')
async def balans(message: types.Message):
    user = db.select_user(id=message.from_user.id)
    text = f"""
    💰Sizning hisobingizda: {user[9]} so'm mavjud

💵 Umumiy ishlagan pullaringiz: {user[9]+user[10]} so'm 
💸 Yechib oldingiz: {user[10]} so'm 

💳 Sizning karta raqamingiz: {user[4]}
📞 Paynet uchun tel nomeringiz: {user[3]}"""

    await message.answer(text=text, reply_markup=balans_keyboard_uz)


@dp.message_handler(text="📋 Qoidalar")
async def rules(message: types.Message):
    rules = db.get_rules()
    text = f"""📋 Qoidalar
   {rules[1]}"""
    
    await message.answer(text=text)


@dp.message_handler(text="👤 Shaxsiy Kabinet")
async def personal_info(message: types.Message):
    user = db.select_user(id=message.from_user.id)
    text = f"""
    👤 Shaxsiy Kabinet

    Assalomu alaykum {message.from_user.first_name}

    ✅ Ism-Familya: {user[2]} 
    ✅ Jinsingiz: {user[11]}
    ✅ Yoshingiz: {user[6]} 
    ✅ Manzil: {user[5]}
    ✅ Tel nomeringiz: {user[3]}

    👥 Do'stlaringiz: {db.count_friends(id=message.from_user.id)} nafar
    📎 Shaxsiy referal linkingiz: https://t.me/pdp_aloqa_bot?start={message.from_user.id}
    """
    
    await message.answer(text=text)
    

@dp.message_handler(text="👨🏻‍💻 Bog'lanish")
async def contact(message: types.Message):
    text = f"{db.get_contact_number()}"
    
    await message.answer(text=text)


@dp.message_handler(text="⚙️ Sozlash")
async def rules(message: types.Message):
    text = f"⚙️ Sozlash"
    
    await message.answer(text=text, reply_markup=settings_keyboard_uz)



@dp.message_handler(text='⬅️')
async def go_to_home(message: types.Message):
    language = db.get_language(id=message.from_user.id)
    if language == 'ru':
        await message.answer(text="Главное меню", reply_markup=main_menu_keyboard_ru)
    elif language == 'en':
        await message.answer(text="Main menu", reply_markup=main_menu_keyboard_en)
    else:
        await message.answer(text="Bosh menyu", reply_markup=main_menu_keyboard_uz)