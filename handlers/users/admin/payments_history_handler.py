from aiogram import types

from loader import dp, db, bot


@dp.message_handler(text="💸 To'lovlar tarixi")
async def payments_history(message: types.Message):
    withdrawns = db.select_all_withdrawns()
    print(withdrawns)
    text = ""
    payment_type = None
    for withdrawn in withdrawns:
        if withdrawn[5] is not None:
            payment_type = "Click Kartaga"
        elif withdrawn[6] is not None:
            payment_type = "Telefon raqamga Paynet "
        text += f"""Pul o'tkazma: {payment_type}
        Kimga: {withdrawn[3]}
        Miqdori: {withdrawn[4]}
        Telefon: {withdrawn[6]}
        Karta: {withdrawn[5]}
        Sana: {withdrawn[7]}
        
        ---------------------------------------

        """
    with open('payment_history.txt', 'w') as f:
        f.write(text)
        print(f, 'just file')
        
    with open('payment_history.txt', 'r') as f:
        print(type(f), "-----------type-------------")
        # await message.answer_document(document=f, caption="To'lovlar tarixi")
        await bot.send_document(message.from_user.id, document=f, caption="To'lovlar tarixi")
