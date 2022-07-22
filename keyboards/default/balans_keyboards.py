from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


balans_keyboard_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📤 Pulni yechib olish")
        ],
        [
            KeyboardButton(text="⬅️"),
        ]  
    ],
resize_keyboard=True)

balans_keyboard_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📤 Withdraw money")
        ],
        [
            KeyboardButton(text="⬅️"),
        ]  
    ],
resize_keyboard=True)

balans_keyboard_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📤 Снять деньги")
        ],
        [
            KeyboardButton(text="⬅️"),
        ]  
    ],
resize_keyboard=True)
# --------------------------------------------------------------- #

withdraw_money_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💳 Click"),
            KeyboardButton(text="🟢 Paynet")
        ],
        [
            KeyboardButton(text="⬅️")
        ]
    ],
resize_keyboard=True)
