from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.keyboards import make_channels_keyboard, yes_no
from states.channels_states import ChannelStates
from loader import dp, db


@dp.message_handler(text='Kanallar')
async def channels(message: types.Message):
    text = f"Kanallar ro'yxati: \n Biror kanalni o'chirish uchun ustiga bosing"
    await message.answer(text, reply_markup=make_channels_keyboard())
    await ChannelStates.channels.set()


@dp.callback_query_handler(text='add_channel', state=ChannelStates.channels)
async def new_channel(callback: types.CallbackQuery):
    await ChannelStates.add_new.set()
    await callback.message.answer("Kanal nomini kiriting:")

@dp.message_handler(state=ChannelStates.add_new)
async def get_new_channel_name(message: types.Message, state: FSMContext):
    await state.update_data({"channel_name":message.text})
    text = "Kanalning Id'sini kiriting:"
    await message.answer(text)
    await ChannelStates.id.set()

@dp.message_handler(state=ChannelStates.id)
async def get_channel_id(message: types.Message, state: FSMContext):
    await state.update_data({'channel_id':message.text})
    text = "Kanalning linkini t.me/kanal_linki ko'rinishida kiriting yoki yopiq kanal bo'lsa taklif havolasini kiriting."
    await message.answer(text)
    await ChannelStates.link.set()
    

@dp.message_handler(state=ChannelStates.link)
async def get_channel_link(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get('channel_name')
    id = data.get('channel_id')
    db.add_channel(name=name, channel_id=id, link=message.text)

    await message.answer("✅ Kanal Qo'shildi \n ❗️Eslatma: bot kanalda admin bo'lishi kerak")
    await state.finish()


@dp.callback_query_handler(state=ChannelStates.channels)
async def delete_channel(callback: types.CallbackQuery, state: FSMContext):
    
    await state.update_data({'channel_id':callback.data})
    for key in callback.message.reply_markup.inline_keyboard:
        if key[0].callback_data == callback.data:
            channel_name = key[0].text
            break

    text = f"Bu kanalni rostan o'chirmoqchimisiz: {channel_name}"
    await callback.message.edit_text(text, reply_markup=yes_no)
    # await callback.message.edit_reply_markup(text, reply_markup=yes_no)
    await ChannelStates.delete.set()


@dp.callback_query_handler(text='yes', state=ChannelStates.delete)
async def confirm_deleting_channel(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    channel_id = data.get('channel_id')
    db.delete_channel(channel_id)
    text = f"Kanallar ro'yxati: \n Biror kanalni o'chirish uchun ustiga bosing"
    await callback.message.edit_text(text, reply_markup=make_channels_keyboard())
    await ChannelStates.channels.set()


@dp.callback_query_handler(text='no', state=ChannelStates.delete)
async def confirm_deleting_channel(callback: types.CallbackQuery):
    text = f"Kanallar ro'yxati: \n Biror kanalni o'chirish uchun ustiga bosing"
    await callback.message.edit_text(text, reply_markup=make_channels_keyboard())
    await ChannelStates.channels.set()

