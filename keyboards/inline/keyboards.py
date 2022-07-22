
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyparsing import col

from loader import db

language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🇺🇿 Uz', callback_data='uz'),
            InlineKeyboardButton(text='🇬🇧 En', callback_data='en'),
            InlineKeyboardButton(text='🇷🇺 Ru', callback_data='ru')
        ]
    ]
)


verify_by_click_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="verify_to_withdraw_by_click"),
            # InlineKeyboardButton(text="Boshqa kartaga yechish", callback_data='withdraw_to_other_card')
        ]
    ]
)
verify_by_click_en = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Confirm", callback_data="verify_to_withdraw_by_click"),
            # InlineKeyboardButton(text="Withdraw on another card", callback_data='withdraw_to_other_card')
        ]
    ]
)
verify_by_click_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Подтверждать", callback_data="verify_to_withdraw_by_click"),
            # InlineKeyboardButton(text="Вывод на другую карту", callback_data='withdraw_to_other_card')
        ]
    ]
)

verify_by_paynet_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="verify_to_withdraw_by_paynet"),
            # InlineKeyboardButton(text="Boshqa telefonga", callback_data="withdraw_to_other_phone")
        ]
    ]
)
verify_by_paynet_en = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Confirm", callback_data="verify_to_withdraw_by_paynet"),
            # InlineKeyboardButton(text="Boshqa telefonga", callback_data="withdraw_to_other_phone")
        ]
    ]
)
verify_by_paynet_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Подтверждать", callback_data="verify_to_withdraw_by_paynet"),
            # InlineKeyboardButton(text="Boshqa telefonga", callback_data="withdraw_to_other_phone")
        ]
    ]
)


edit_rules_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🇺🇿 Uz - O\'zgartirish uchun bosing', callback_data='change_rules_uz'),
        ],
        [
            InlineKeyboardButton(text='🇺🇸 En - Click to change', callback_data='change_rules_en'),
        ],
        [
            InlineKeyboardButton(text='🇷🇺 Ru - Нажмите, чтобы изменить', callback_data='change_rules_ru')
        ]
    ]
)


yes_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha", callback_data='yes'),
            InlineKeyboardButton(text="Yo'q", callback_data='no')
        ]
    ]
)

gender_keyboard_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Erkak", callback_data='1'),
            InlineKeyboardButton(text="Ayol", callback_data='0')
        ]
    ]
)
gender_keyboard_en = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Male", callback_data='1'),
            InlineKeyboardButton(text="Female", callback_data='0')
        ]
    ]
)
gender_keyboard_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Мужской", callback_data='1'),
            InlineKeyboardButton(text="Женщина", callback_data='0')
        ]
    ]
)
def withdrawn_keyboard(callback_id):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="To'landi", callback_data=f'withdrawn_to:{callback_id}')
            ]
        ]
    )
    return keyboard


def channels_list_for_subscription():
    keyboard = InlineKeyboardMarkup()
    channels_list = db.get_channels()
   
    for channel in channels_list:
        keyboard.add(InlineKeyboardButton(text=channel[1], url=f"{channel[2]}"))

    keyboard.add(InlineKeyboardButton(text='✅', callback_data="check_subscription"))
    return keyboard

def make_channels_keyboard():
    channels_list = db.get_channels()
    channels_keyboard = InlineKeyboardMarkup()
    
    for channel in channels_list:
        channels_keyboard.add(InlineKeyboardButton(text=channel[1], callback_data=f"{channel[0]}"))

    channels_keyboard.add(InlineKeyboardButton(text="Yangi qo'shish", callback_data="add_channel"))
    return channels_keyboard

