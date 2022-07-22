from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


main_menu_keyboard_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🤑 Pul ishlash")
        ],
        [
            KeyboardButton(text="Balans 🤑"),
            KeyboardButton(text="👤 Shaxsiy Kabinet"),
        ],
        [
            KeyboardButton(text="📋 Qoidalar"),
            KeyboardButton(text="👨🏻‍💻 Bog'lanish"),
        ],
        [
            KeyboardButton(text="⚙️ Sozlash")
        ]
    ],
resize_keyboard=True)

main_menu_keyboard_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🤑 Make money")
        ],
        [
            KeyboardButton(text="Balance 🤑"),
            KeyboardButton(text="👤 Personal Cabinet"),
        ],
        [
            KeyboardButton(text="📋 Rules"),
            KeyboardButton(text="👨🏻‍💻 Contact"),
        ],
        [
            KeyboardButton(text="⚙️ Settings")
        ]
    ],
resize_keyboard=True)

main_menu_keyboard_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🤑 Зарабатывать")
        ],
        [
            KeyboardButton(text="Баланс 🤑"),
            KeyboardButton(text="👤 Личный кабинет"),
        ],
        [
            KeyboardButton(text="📋 Правила"),
            KeyboardButton(text="👨🏻‍💻 Контакт"),
        ],
        [
            KeyboardButton(text="⚙️ Настройки")
        ]
    ],
resize_keyboard=True)