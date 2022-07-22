
from distutils.util import change_root
from aiogram import types


from loader import dp, db, bot

@dp.callback_query_handler(text_contains="withdrawn_to:")
async def withdrawn_to(callback: types.CallbackQuery):
    callback_id = callback.data.split(':')[1]
    db.set_withdrawn(callback_id[1])
    db.withdrawn(db.get_user_id(callback_id=callback_id), db.get_amount(callback_id=callback_id))
    text = callback.message.text
    text += "\n ✅ To'langan"
    await callback.answer("Status ✅ To'langan bo'ldi")
    await callback.message.edit_text(text, reply_markup=None)
    await bot.send_message(chat_id=db.get_user_id(callback_id=callback_id), text="So'rovingiz admin Tomonidan tasdiqlandi, Hisobingizga pul o'tkazildi")