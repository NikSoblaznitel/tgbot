from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Про Масела')
b2 = KeyboardButton('Про Эмаря')
b3 = KeyboardButton('Про Васька')
b4 = KeyboardButton('Про Мишаню')
b5 = KeyboardButton('Про Сизова')
b6 = KeyboardButton('Про Леху')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6)