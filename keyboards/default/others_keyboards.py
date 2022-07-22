from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

concat_button = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='📞 Share contact', request_contact=True),
        ],
    ],
    resize_keyboard=True
)


reply_keyboard_remove=ReplyKeyboardRemove(selective = None)



