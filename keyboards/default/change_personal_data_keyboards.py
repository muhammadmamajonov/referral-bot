
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


change_personal_data_keyboard_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yoshni o'zgartirish")
        ],
        [
            KeyboardButton(text="Manzilni o'zgartirish"),
        ],
        [
            KeyboardButton(text="⬅️"),
        ]  
    ],
resize_keyboard=True)

change_personal_data_keyboard_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Change age")
        ],
        [
            KeyboardButton(text="Change address"),
        ],
        [
            KeyboardButton(text="⬅️"),
        ]  
    ],
resize_keyboard=True)

change_personal_data_keyboard_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Изменить возраст")
        ],
        [
            KeyboardButton(text="Сменить адрес"),
        ],
        [
            KeyboardButton(text="⬅️"),
        ]  
    ],
resize_keyboard=True)