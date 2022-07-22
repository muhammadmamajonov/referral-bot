from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.settings_keyboards import  settings_keyboard_en
from keyboards.default.make_money_keyboards import make_money_menu_keyboard_en
from keyboards.default.main_manu_keyboards import main_menu_keyboard_uz, main_menu_keyboard_ru, main_menu_keyboard_en
from keyboards.default.balans_keyboards import balans_keyboard_en
from loader import dp, db


@dp.message_handler(text='🤑 Make money')
async def make_money(message: types.Message):
    await message.answer("Make money 🤑 ", reply_markup=make_money_menu_keyboard_en)


@dp.message_handler(text='Balance 🤑')
async def balans(message: types.Message):
    user = db.select_user(id=message.from_user.id)
    text = f"""
    💰You have {user[9]} UZS in your account

💵 Your total earned money: {user[9]+user[10]} UZS 
💸 Withdrawn: {user[10]} UZS 

💳 Your card number: {user[4]}
📞 Your phone number for Paynet: {user[3]}"""

    await message.answer(text=text, reply_markup=balans_keyboard_en)


@dp.message_handler(text="📋 Rules")
async def rules(message: types.Message):
    rules = db.get_rules()
    text = f"""📋 Rules
    {rules[2]}"""
    
    await message.answer(text=text)


@dp.message_handler(text="👤 Personal Cabinet")
async def personal_info(message: types.Message):
    user = db.select_user(id=message.from_user.id)
    text = f"""
    👤 Personal Cabinet

    Hello {message.from_user.first_name} 

    ✅ Full name: {user[2]} 
    ✅ Gender: {user[11]}
    ✅ Age: {user[6]} 
    ✅ Address: {user[5]}
    ✅ Phone number: {user[3]}

    👥 Friends: {db.count_friends(id=message.from_user.id)} 
    📎 Your personal referral link: https://t.me/pdp_aloqa_bot?start={message.from_user.id}
    """
    
    await message.answer(text=text)
    

@dp.message_handler(text="👨🏻‍💻 Contact")
async def contact(message: types.Message):
    text = f"{db.get_contact_number()}"
    
    await message.answer(text=text)


@dp.message_handler(text="⚙️ Settings")
async def rules(message: types.Message):
    text = f"⚙️ Settings"
    
    await message.answer(text=text, reply_markup=settings_keyboard_en)
