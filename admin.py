# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram import types, Dispatcher
# from keyboards import kb_client
# from aiogram.types import ReplyKeyboardRemove
# from bot import dp
#
# class FSMAdmin(StatesGroup):
#     name = State()
#     phrase = State()
#
# dt = []
#
# #@dp.message_handler(commands=['add_text'], state=None)
# async def add_text(message: types.Message):
#         await FSMAdmin.name.set()
#         await message.reply('Для кого добавить фразу?', reply_markup=kb_client)
#
# #@dp.message_handler(state=FSMAdmin.name)
# async def add_name(message: types.Message, state: FSMContext):
#         async with state.proxy() as data:
#             dt[0] = message.text
#         await FSMAdmin.next
#         await message.reply('Введи текст сообщения', reply_markup=ReplyKeyboardRemove)
#
# #@dp.message_handler(state=FSMAdmin.phrase)
# async def add_pharase(message: types.Message, state: FSMContext):
#         async with state.proxy() as data:
#             dt[1] = message.text
#
#         await state.finish()
#
# def register_handlers_admin(dp: Dispatcher):
#     @dp.message_handler(add_text, commands=['add_text'], state=None)
#     @dp.message_handler(add_name, state=FSMAdmin.name)
#     @dp.message_handler(add_pharase, state=FSMAdmin.phrase)