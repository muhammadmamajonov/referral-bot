from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_settings_menu_keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="📞 Bog'lanish uchun raqamni o'zgartirish"),
        ],
        [
            KeyboardButton(text='💸 Taklif uchun narxni belgilash'),
        ],
        [
            KeyboardButton(text="◀️ Ortga")
        ]
    ],
resize_keyboard=True)