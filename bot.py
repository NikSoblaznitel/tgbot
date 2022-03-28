import config_bydlo
import logging
from random import randint
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

logging.basicConfig(level=logging.INFO)

storage=MemoryStorage()

bot = Bot(token=config_bydlo.TOKEN)
dp = Dispatcher(bot, storage=storage)

class FSMAdmin(StatesGroup):
    name = State()
    song = State()

dt = ['a','b']

@dp.message_handler(commands=['add_text'], state=None)
async def add_text(message: types.Message):
        await FSMAdmin.name.set()
        await bot.send_message(message.from_user.id, 'Про кого добавить фразу?', reply_markup=kb_client)
        await message.delete()

@dp.message_handler(state=FSMAdmin.name)
async def add_name(message: types.Message, state: FSMContext):

        dt[0] = message.text
        await FSMAdmin.next()
        await message.reply('Введи текст сообщения')

@dp.message_handler(state=FSMAdmin.song)
async def add_song(message: types.Message, state: FSMContext):

        dt[1] = message.text
        await message.reply(dt)
        w = open(F'library/{dt[0]}.txt', 'a')
        w.write(dt[1] + '\n')
        w.close()
        await state.finish()


# @dp.message_handler()
# async def piisya(message: types.Message):
#         z = open(F'newid.txt', 'a')
#         z.write(F'{message.from_user.id}' + ' : ' + F'{message.from_user.username}' + '\n')
#         z.close()


@dp.message_handler()
async def bydlo(message: types.Message):
    chek = message.text.split(' ')
    # chek = achek.split(' ')
    for i in chek:
        if i == '@bydlosims_bot' or i == 'Быдло' or i == 'волчара' \
                or i == 'Волчара' or i == 'быдло' or i == 'Хуесос' or i == 'хуесос':
            Name = str(message.from_user.id)
            if Name == "72917581":
                libN = []
                with open('library/Про Масела.txt', 'r') as file:
                    for line in file:
                        n = line.replace('\n', '')
                        libN = libN + [n]
                how = len(libN)
                RND = randint(0, how - 1)
                await message.reply(libN[RND])
            elif Name == "195976776":
                libN = []
                with open('library/Про Эмаря.txt', 'r') as file:
                    for line in file:
                        n = line.replace('\n', '')
                        libN = libN + [n]
                how = len(libN)
                RND = randint(0, how - 1)
                await message.reply(libN[RND])
            elif Name == "359000449":
                libN = []
                with open('library/Про Васька.txt', 'r') as file:
                    for line in file:
                        n = line.replace('\n', '')
                        libN = libN + [n]
                how = len(libN)
                RND = randint(0, how - 1)
                await message.reply(libN[RND])
            elif Name == "733518869":
                libN = []
                with open('library/Про Мишаню.txt', 'r') as file:
                    for line in file:
                        n = line.replace('\n', '')
                        libN = libN + [n]
                how = len(libN)
                RND = randint(0, how - 1)
                await message.reply(libN[RND])
            elif Name == "370591881":
                libN = []
                with open('library/Про Сизова.txt', 'r') as file:
                    for line in file:
                        n = line.replace('\n', '')
                        libN = libN + [n]
                how = len(libN)
                RND = randint(0, how - 1)
                await message.reply(libN[RND])
            elif Name == "423160295":
                libN = []
                with open('library/Про Леху.txt', 'r') as file:
                    for line in file:
                        n = line.replace('\n', '')
                        libN = libN + [n]
                how = len(libN)
                RND = randint(0, how - 1)
                await message.reply(libN[RND])
            else:
                await message.answer("Ты кто такой? Представься.")




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
