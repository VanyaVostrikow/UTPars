from aiogram import Bot, Dispatcher, executor, types
from SpecFunc import make_keyboards
from SpecFunc.Users import User
from SpecFunc.Subscribe import Subscribe
from SpecFunc.Template import Template
from aiogram.types import InputFile
import asyncio
from datetime import datetime, timedelta
from random import randint
from bot import Settings
import os
bot = Bot(token=Settings.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    user = await User(message.chat.id).check_user()
    keyboard = await make_keyboards.make_first_key()
    await message.reply("Привет!)", reply_markup= keyboard)
@dp.message_handler(commands='admin')
async def admin_cmd(message: types.Message):
    if str(message.chat.id) in (Settings.ADMINS):
        await bot.send_message(message.chat.id, f'<b>Привет,{message.chat.first_name}, Вы в админской панели</b>')
    else:
        await bot.send_message(message.chat.id, "Неизвестная комманда")





@dp.message_handler()
async def start_test(message: types.Message):
    if message.text == 'Добавить отслеживаемый канал':
        print(2)
        await bot.send_message(message.chat.id, 'Введите ссылку(youtube/) или id(@) канала:')
    elif message.text == 'Получить список каналов':
        print(0)
        a = await Subscribe(message.chat.id).get_list()
        html = await Template().list_subscribe(a)
        await bot.send_message(message.chat.id, str(html), parse_mode='HTML')
    elif message.text == 'Получить видео сейчас':
        print(1)
        pass
    elif message.text.startswith('youtube/') or message.text.startswith('@'):
        channel = Subscribe(message.chat.id)
        print(message.text)
        await channel.add_chanell(message.text)
    elif message.text.startswith('?'):
        link = message.text.split('?')[1]
        res = await Subscribe(message.chat.id).unsub_from_channel(link)
        if res == True:
            await bot.send_message(message.chat.id, "Channel "+link+"UNSUB!")
        else:
            await bot.send_message(message.chat.id, "А вы подписаны на " + link + "?")

async def start():
        try:
            await dp.start_polling(bot)
        except:
            session = await bot.get_session()
            await session.close()
            await bot.session.close()
            #await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(start())
    except (KeyboardInterrupt, SystemExit):
        pass