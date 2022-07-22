
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


settings_keyboard_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌐 Tilni tanlash")
        ],
        [
            KeyboardButton(text="💳 Hisob raqamni almashtirish"),
        ],
        [
            KeyboardButton(text="👤 Shaxsiy ma'lumotlarni o'zgartirish"),
        ],
        [
            KeyboardButton(text="⬅️"),
        ]  
    ],
resize_keyboard=True)

settings_keyboard_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌐 Select language")
        ],
        [
            KeyboardButton(text="💳 Change account number"),
        ],
        [
            KeyboardButton(text="👤 Change of personal data"),
        ],
        [
            KeyboardButton(text="⬅️"),
        ]  
    ],
resize_keyboard=True)

settings_keyboard_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌐 Выбор языка")
        ],
        [
            KeyboardButton(text="💳 Изменить номер счета"),
        ],
        [
            KeyboardButton(text="👤 Изменение персональных данных"),
        ],
        [
            KeyboardButton(text="⬅️"),
        ]  
    ],
resize_keyboard=True)

# --------------------------------------- #
change_account_number_keyboard_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💳 Click raqamini o'zgartirish"),
        ],
        [
            KeyboardButton(text="📞 Tel nomerni o'zgartirish"),
        ],
        [
            KeyboardButton(text="⬅️"),
        ]
    ]
)

change_account_number_keyboard_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💳 Change the Click number"),
        ],
        [
            KeyboardButton(text="📞 Change the phone number"),
        ],
        [
            KeyboardButton(text="⬅️"),
        ]
    ]
)

change_account_number_keyboard_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💳 Изменить номер Click"),
        ],
        [
            KeyboardButton(text="📞 Изменить номер телефона"),
        ],
        [
            KeyboardButton(text="⬅️"),
        ]
    ]
)