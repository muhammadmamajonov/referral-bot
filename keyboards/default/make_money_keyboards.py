from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


make_money_menu_keyboard_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👥 Do'stlarni taklif qilish")
        ],
        # [
        #     KeyboardButton(text="📲 Vazifa bajarish"),
        # ],
        [
            KeyboardButton(text="⬅️"),
        ]  
    ],
resize_keyboard=True)

make_money_menu_keyboard_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👥 Invite friends")
        ],
        # [
        #     KeyboardButton(text="📲 Task performance"),
        # ],
        [
            KeyboardButton(text="⬅️"),
        ]  
    ],
resize_keyboard=True)

make_money_menu_keyboard_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👥 Пригласить друзей")
        ],
        # [
        #     KeyboardButton(text="📲 Выполнение задач"),
        # ],
        [
            KeyboardButton(text="⬅️"),
        ]  
    ],
resize_keyboard=True)