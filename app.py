from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    #Ma'lumotlar omboriga jadvallarni qo'shamiz
    try:
        db.create_table_withdraws()
        db.create_table_users()
        db.create_table_other_settings()
        db.create_table_channels()
        db.create_table_rules()
    except:
        pass
    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
