from cgitb import text
from datetime import datetime
from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.balans_keyboards import withdraw_money_keyboard, balans_keyboard_en, balans_keyboard_ru, balans_keyboard_uz
from keyboards.inline.keyboards import verify_by_paynet_ru, verify_by_paynet_en, verify_by_paynet_uz, verify_by_click_ru, verify_by_click_en, verify_by_click_uz, withdrawn_keyboard
from states.withdraw_money_state import WithdrawMoney
from loader import dp, bot, db
from data.config import ADMINS


@dp.message_handler(text='📤 Pulni yechib olish')
async def make_money_uz(message: types.Message):
    await message.answer("👇 To'lov turini tanlang", reply_markup=withdraw_money_keyboard)
    await WithdrawMoney.in_withdraw.set()

@dp.message_handler(text='📤 Withdraw money')
async def make_money_en(message: types.Message):
    await message.answer("👇 Select the payment type", reply_markup=withdraw_money_keyboard)
    await WithdrawMoney.in_withdraw.set()

@dp.message_handler(text='📤 Снять деньги')
async def make_money_ru(message: types.Message):
    await message.answer("👇 Выберите тип оплаты", reply_markup=withdraw_money_keyboard)
    await WithdrawMoney.in_withdraw.set()


# ----------- Click ----------- #
@dp.message_handler(text="💳 Click", state=WithdrawMoney.in_withdraw)
async def click(message: types.Message):
    language = db.get_language(id=message.from_user.id)
    if language == 'en':
        text = f"""
        Your Click number: {db.get_card_num(id=message.from_user.id)}
        If you want to withdraw money to another card, change the card number from the <b>⚙️ Settings</b> section
        """
        await message.answer(text=text, reply_markup=verify_by_click_en)
    elif language == 'ru':
        text = f"""
        Ваш номер Click: {db.get_card_num(id=message.from_user.id)}
        Если вы хотите вывести деньги на другую карту, измените номер карты в разделе <b>⚙️ Настройки</b>
        """
        await message.answer(text=text, reply_markup=verify_by_click_ru)
    else:
        text = f"""
        Click raqamingiz: {db.get_card_num(id=message.from_user.id)}
        Agar boshqa kartaga pul yechmoqchi bo'lsangiz <b>⚙️ Sozlash</b> bo'limidan karta raqamini o'zgartiring
        """
        await message.answer(text=text, reply_markup=verify_by_click_uz)



@dp.callback_query_handler(text="verify_to_withdraw_by_click", state=WithdrawMoney.in_withdraw)
async def withdraw_by_click(callback: types.CallbackQuery):
    user = db.select_user(id=callback.from_user.id)
   
    withdraw = db.add_withdraw(callback_id=callback.id, user_id=callback.from_user.id, to=user[2], amount=user[9], card_num=db.get_card_num(id=callback.from_user.id))
    
    dtime = datetime.now()
    dtime = f"{dtime.year}-{dtime.month}-{dtime.day} {dtime.hour}:{dtime.minute}"
    text = f"""Pul o'tkazish kerak <b>Click</b> orqali {db.get_card_num(id=callback.from_user.id)}
    <b>Kimga:</b> {user[2]}
    <b>Miqdori:</b> {user[9]}
    <b>Telefon:</b> {db.get_phone_num(id=callback.from_user.id)}
    <b>Sana:</b> {dtime}"""
    await bot.send_message(ADMINS[0], text=text, reply_markup=withdrawn_keyboard(callback.id))

    language = db.get_language(id=callback.from_user.id)
    await callback.message.delete()
    if language == 'en':
        await callback.message.answer("Your request has been sent to the admin. Money will be transferred to your account if it is reviewed and approved by the admin")
    elif language == 'ru':
        await callback.message.answer("Ваша заявка отправлена ​​администратору. Деньги будут переведены на ваш счет, если он будет рассмотрен и одобрен администратором.")
    else:
        await callback.message.answer("So'rovingiz adminga yuborildi. Admin tomonidan ko'rib chiliqilib tasdiqlansa hisobingizga pul o'tkazib beriliadi")

# ----------- Paynet ----------- #
@dp.message_handler(text="🟢 Paynet", state=WithdrawMoney.in_withdraw)
async def paynet(message: types.Message):
    
    language = db.get_language(id=message.from_user.id)
    if language == 'en':
        text = f"""
        Your phone number for Paynet: {db.get_phone_num(message.from_user.id)}
        If you want to transfer money to another phone number, change the phone number from the <b>⚙️ Settings</b> section
        """
        await message.answer(text=text, reply_markup=verify_by_paynet_en)
    elif language == 'ru':
        text = f"""
        Ваш номер телефона для Paynet: {db.get_phone_num(message.from_user.id)}
        Если вы хотите перевести деньги на другой номер телефона, измените номер телефона в разделе <b>⚙️ Настройки</b>
        """
        await message.answer(text=text, reply_markup=verify_by_paynet_ru)
    else:
        text = f"""
        Paynet uchun tel nomeringiz: {db.get_phone_num(message.from_user.id)}
        Agar siz boshqa telefon raqamiga pul o'tkazmoqchi bo'lsangiz, telefon raqamini <b>⚙️ Sozlash</b> bo'limidan o'zgartiring
        """
        await message.answer(text=text, reply_markup=verify_by_paynet_uz)

 

@dp.callback_query_handler(text="verify_to_withdraw_by_paynet", state=WithdrawMoney.in_withdraw)
async def withdraw_by_paynet(callback: types.CallbackQuery):
    user = db.select_user(id=callback.from_user.id)
   
    withdraw = db.add_withdraw(callback_id=callback.id, user_id=callback.from_user.id, to=user[2], amount=user[9], phone_num=db.get_phone_num(id=callback.from_user.id))
    
    dtime = datetime.now()
    dtime = f"{dtime.year}-{dtime.month}-{dtime.day} {dtime.hour}:{dtime.minute}"
    text = f"""Pul o'tkazish kerak <b>Paynet</b> orqali {db.get_phone_num(id=callback.from_user.id)}
    <b>Kimga:</b> {user[2]}
    <b>Miqdori:</b> {user[9]}
    <b>Telefon:</b> {db.get_phone_num(id=callback.from_user.id)}
    <b>Sana:</b> {dtime}"""
    await bot.send_message(ADMINS[0], text=text, reply_markup=withdrawn_keyboard(callback.id))

    language = db.get_language(id=callback.from_user.id)
    await callback.message.delete()
    if language == 'en':
        await callback.message.answer("Your request has been sent to the admin. Money will be transferred to your account if it is reviewed and approved by the admin")
    elif language == 'ru':
        await callback.message.answer("Ваша заявка отправлена ​​администратору. Деньги будут переведены на ваш счет, если он будет рассмотрен и одобрен администратором.")
    else:
        await callback.message.answer("So'rovingiz adminga yuborildi. Admin tomonidan ko'rib chiliqilib tasdiqlansa hisobingizga pul o'tkazib beriliadi")


@dp.message_handler(text='⬅️', state=WithdrawMoney.in_withdraw)
async def go_back(message: types.Message, state: FSMContext):
    language = db.get_language(id=message.from_user.id)
    if language == 'en':
        await message.answer(text="Balance menu", reply_markup=balans_keyboard_en)
    elif language == 'ru':
        await message.answer(text="Меню баланса", reply_markup=balans_keyboard_ru)
    else:
        await message.answer(text="Balans menyu", reply_markup=balans_keyboard_uz)
    await state.finish()


