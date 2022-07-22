from aiogram import types
from aiogram.dispatcher import FSMContext
from states.registration_states import Registration
from keyboards.inline.confirmation_consent_keyboard import consent_uz, consent_en, consent_ru
from keyboards.default.others_keyboards import concat_button, reply_keyboard_remove
from keyboards.default.main_manu_keyboards import main_menu_keyboard_uz, main_menu_keyboard_en, main_menu_keyboard_ru
from keyboards.inline.keyboards import channels_list_for_subscription, gender_keyboard_ru, gender_keyboard_en, gender_keyboard_uz

from loader import dp, db, bot


@dp.callback_query_handler(state=Registration.language_seletction)
async def set_lang(call: types.CallbackQuery):
    await Registration.rules.set()
    
    db.set_language(id=call.from_user.id, language=call.data)

    await call.message.delete()
    rules = db.get_rules()

    if call.data == 'ru':
        await call.message.answer(f"""
        📃 Смотрите правила!
{rules[3]}""", reply_markup=consent_ru)
    elif call.data == 'en':
        await call.message.answer(f"""
        📃 See the rules!
{rules[2]}""", reply_markup=consent_en)
    else:
        await call.message.answer(f"""
        📃 Qoidalar bilan tanishing!
{rules[1]}""", reply_markup=consent_uz)


@dp.callback_query_handler(text='agree', state=Registration.rules)
async def rules_agree(call: types.CallbackQuery):
    
    await Registration.next()
    await call.message.delete()
    language = db.get_language(id=call.from_user.id)

    if language == 'ru':
        await call.message.answer("Нажмите кнопку ниже, чтобы отправить свой номер телефона", reply_markup=concat_button)
    elif language == 'en':
        await call.message.answer("Press the button below to send your phone number", reply_markup=concat_button)
    else:
        await call.message.answer("Telefon raqamingizni yuborish uchun pastdagi tugmani bosing", reply_markup=concat_button)


@dp.message_handler(content_types=types.ContentType.CONTACT, state=Registration.contact_share)
async def get_phone(message: types.Message, state: FSMContext):
   
    await Registration.next()

    await state.update_data(
        {"phone": message.contact.phone_number}
    )
    
    language = db.get_language(id=message.from_user.id)

    if language == 'ru':
        await message.answer("Введите свой адрес", reply_markup=reply_keyboard_remove)
    elif language == 'en':
        await message.answer("Enter your address", reply_markup=reply_keyboard_remove)
    else:
        await message.answer("Manzilingizni kiriting", reply_markup=reply_keyboard_remove)


@dp.message_handler(state=Registration.address)
async def get_address(message: types.Message, state: FSMContext):
    await Registration.next()
    
    await state.update_data(
        {"address": message.text}
    )

    language = db.get_language(id=message.from_user.id)

    if language == 'ru':
        await message.answer("Введите свое имя и фамилию.")
    elif language == 'en':
        await message.answer("Enter your full name.")
    else:
        await message.answer("Ism va familyangizni kiriting.")

@dp.message_handler(state=Registration.fullName)
async def get_fullname(message: types.Message, state: FSMContext):
    language = db.get_language(id=message.from_user.id)
    await state.update_data({'full_name':message.text})
    
    if language == 'en':
        await message.answer("Select", reply_markup=gender_keyboard_en)
    elif language == 'ru':
        await message.answer("Выбирать", reply_markup=gender_keyboard_ru)
    else:
        await message.answer("Tanlang", reply_markup=gender_keyboard_uz)
    await Registration.gender.set()

@dp.callback_query_handler(state=Registration.gender)   
async def select_gender(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    gender = callback.data
    address = data.get('address')
    phone = data.get('phone')
    full_name = data.get('full_name')

    db.edit_user(id=callback.from_user.id, full_name=full_name, phone=phone, address=address, gender=gender)
    await state.finish()
    language = db.get_language(id=callback.from_user.id)

    if language == 'ru':
        await callback.message.edit_text("Подпишитесь на следующие каналы и нажмите кнопку ✅.", reply_markup=channels_list_for_subscription())    
    elif language == 'en':
        await callback.message.edit_text("Subscribe to the following channels and click the ✅ button.", reply_markup=channels_list_for_subscription())
    else:
        await callback.message.edit_text("Quyidagi kanallarga obuna bo'lib ✅ tugmasini bosing.", reply_markup=channels_list_for_subscription())


@dp.callback_query_handler(text='check_subscription')
async def check_subscription(callback: types.CallbackQuery):
    channels_list = db.get_channels()
    statuses = []
    for channel in channels_list:
        check = await bot.get_chat_member(channel[0], callback.from_user.id)
        statuses.append(check.status)
    print(callback.from_user.id, f"<<<<<<<<<<<<<<<<<<<<<--------ID:{callback.from_user.id},--------->>>>>>>>>>>>>>>>>>>>>>>")
    language = db.get_language(id=callback.from_user.id)
    if 'left' in statuses:
        if language == 'ru':
            await callback.answer("Подписывайтесь на все каналы")
        elif language == 'en':
            await callback.answer("Subscribe to all channels")
        else:
            await callback.answer("Barcha kanallarga obuna bo'ling")
    else:
        referer_id = db.get_referer(user_id=callback.from_user.id)
        if referer_id is not None:
            referer_language = db.get_language(referer_id)
            db.add_money_to_earnings(referer_id)
            if referer_language == 'en':
                text = f"{callback.from_user.first_name} registered through your invitation link"
            elif referer_language == 'ru':
                text = f"{callback.from_user.first_name} зарегистрировался по вашей пригласительной ссылке"
            else:
                text = f"{callback.from_user.first_name} sizning taklif havolangiz orqali ro'yxatdan o'tdi "
            bot.send_message(referer_id, text=text)
            
        if language == 'ru':
            await callback.message.answer("Вы можете использовать бота", reply_markup=main_menu_keyboard_ru)
        elif language == 'en':
            await callback.message.answer("You can use a bot", reply_markup=main_menu_keyboard_en)
        else:
            await callback.message.answer(f"Botdan foydalanishingiz mumkin", reply_markup=main_menu_keyboard_uz)
            
        
  