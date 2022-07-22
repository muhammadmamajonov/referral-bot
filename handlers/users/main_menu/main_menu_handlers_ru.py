from aiogram import types
from keyboards.default.settings_keyboards import  settings_keyboard_ru
from keyboards.default.make_money_keyboards import make_money_menu_keyboard_ru
from keyboards.default.main_manu_keyboards import  main_menu_keyboard_ru
from keyboards.default.balans_keyboards import balans_keyboard_ru
from loader import dp, db


@dp.message_handler(text='🤑 Зарабатывать')
async def make_money(message: types.Message):
    await message.answer("Зарабатывать 🤑 ", reply_markup=make_money_menu_keyboard_ru)


@dp.message_handler(text='Баланс 🤑')
async def balans(message: types.Message):
    user = db.select_user(id=message.from_user.id)
    text = f"""
    💰На вашем счету {user[9]} сумов

💵 Сумма ваших заработанных денег {user[9]+user[10]} сумов
💸 Вы взяли свои деньги: {user[10]} сумов

💳 Номер вашей карты: {user[4]}
📞 Ваш номер телефона для Paynet: {user[3]}"""

    await message.answer(text=text, reply_markup=balans_keyboard_ru)


@dp.message_handler(text="📋 Правила")
async def rules(message: types.Message):
    rules = db.get_rules()
    text = f"""📋 Правила
    {rules[3]}"""
    
    await message.answer(text=text)


@dp.message_handler(text="👤 Личный кабинет")
async def personal_info(message: types.Message):
    user = db.select_user(id=message.from_user.id)
    text = f"""
    👤 Личный кабинет

    Здравствуйте {message.from_user.first_name} 

    ✅ Имя и фамилия: {user[2]} 
    ✅ Пол: {user[11]}
    ✅ Ваш возраст: {user[6]} 
    ✅ Адрес: {user[5]}
    ✅ Ваш номер телефона: {user[3]}

    👥 Твои друзья: {db.count_friends(id=message.from_user.id)} 
    📎 Ваша личная реферальная ссылка: https://t.me/pdp_aloqa_bot?start={message.from_user.id}
    """
    
    await message.answer(text=text)
    

@dp.message_handler(text="👨🏻‍💻 Контакт")
async def contact(message: types.Message):
    text = f"{db.get_contact_number()}"
    
    await message.answer(text=text)


@dp.message_handler(text="⚙️ Настройки")
async def rules(message: types.Message):
    text = f"⚙️ Настройки"
    
    await message.answer(text=text, reply_markup=settings_keyboard_ru)
