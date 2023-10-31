from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.make_money_keyboards import make_money_menu_keyboard_en, make_money_menu_keyboard_ru, make_money_menu_keyboard_uz
from loader import dp, db


@dp.message_handler(text="👥 Do'stlarni taklif qilish")
async def invate_friends(message: types.Message):
    text = f"""
    📎 Ushbu referal linkini do'stlaringizga yuboring 👉 https://t.me/referral_bot?start={message.from_user.id}

🤖 Botdan har bir ro'yxatdan o'tgan do'stingiz uchun sizga {db.get_price_for_invited()} so'm to'lanadi

💸 Pullaringizni paynet orqali yoki karta raqamingizga yechib olishingiz mumkin"""
    await message.answer(text=text)


@dp.message_handler(text="📲 Vazifa bajarish")
async def task_performance(message: types.Message):
    text = f"📲 Internetda vazifa bajarib pul ishlash"
    await message.answer(text)

# ---------- English ------------ #
@dp.message_handler(text="👥 Invite friends")
async def invate_friends_en(message: types.Message):
    text = f"""
    📎 Send this referral link to your friends 👉 https://t.me/referral_bot?start={message.from_user.id}

🤖 You will be charged {db.get_price_for_invited()} sums for each registered friend of the bot

💸 You can withdraw your money via paynet or to your card number"""
    await message.answer(text=text)


@dp.message_handler(text="📲 Task performance")
async def task_performance(message: types.Message):
    text = f"📲 Make money by doing tasks on the internet"
    await message.answer(text)

# -------- Russien -----------#
@dp.message_handler(text="👥 Пригласить друзей")
async def invate_friends_ru(message: types.Message):
  
    text = f"""
    📎 Отправьте эту реферальную ссылку своим друзьям 👉 https://t.me/referral_bot?start={message.from_user.id}

🤖 За каждого зарегистрированного друга бота с вас будет начисляться {db.get_price_for_invited()} сумов

💸 Вы можете вывести свои деньги через paynet или на номер карты"""
    await message.answer(text=text)


@dp.message_handler(text="📲 Выполнение задач")
async def task_performance(message: types.Message):
    text = f"📲 Заработок выполняя задания в интернете"
    await message.answer(text)
