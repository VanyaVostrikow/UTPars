from aiogram import types


async def make_first_key():
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Добавить отслеживаемый канал'))
    keyboard.add(types.KeyboardButton('Получить список каналов'))
    keyboard.add(types.KeyboardButton('Получить видео сейчас'))
    return keyboard

async def sub_list(chanels:list=None):
    keyboard = types.InlineKeyboardMarkup
    keyboard.add()