from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_main_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="💸 To'lovlar tarixi"),
            KeyboardButton(text='⚙️ Sozlamalar'),
        ],
        [
            KeyboardButton(text='Kanallar'),
            KeyboardButton(text='🔔 Qoidalarni sozlash'),
        ],
    ],
    resize_keyboard=True
)