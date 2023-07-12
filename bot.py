import aiogram
from aiogram.utils import executor
import asyncio
import json
import aiofiles
import datetime
from settings import *
from strings import *

'''
video id
1| BAACAgIAAxkBAAMpZKq5loNVuQobRJr0e78QCYBGSCMAAu8yAAK-60lJVVxeHciv-6YvBA
2| BAACAgIAAxkBAAMqZKq8aWu-QlwSLOezgl6Loxa8dycAAvIyAAK-60lJ_3ehS50JDoQvBA
3| BAACAgIAAxkBAAMrZKq8clkDR1gAAV0AAfOsFde63pxtpQAC9DIAAr7rSUkNXaBYT_B3OC8E

'''


bot = aiogram.Bot(TOKEN, parse_mode=aiogram.types.ParseMode.HTML)
dp = aiogram.Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: aiogram.types.Message):
    try:await bot.send_message(372512859, 'Бот активирован новым человеком')
    except:pass
    await message.answer(FIRST_MESSAGE)
    await asyncio.sleep(25)
    await message.answer(SECOND_MESSAGE)
    await asyncio.sleep(25)
    keyboard = aiogram.types.InlineKeyboardMarkup(2)
    keyboard.add(aiogram.types.InlineKeyboardButton('НАЧАТЬ ОБУЧЕНИЕ ✅', callback_data='next_1'))
    keyboard.add(aiogram.types.InlineKeyboardButton('ЗАДАТЬ ВОПРОС ТРЕЙДЕРУ🤔', url='https://t.me/mhtrade_bo'))
    await message.answer(THIRD_MESSAGE, reply_markup=keyboard)
    await create_task(message.from_user.id, 4, str(datetime.datetime.now()+datetime.timedelta(days=1)))
    await asyncio.sleep(1)

@dp.callback_query_handler(text='next_1')
async def next_1(callback: aiogram.types.CallbackQuery):
    user_id = callback.from_user.id
    async with aiofiles.open('tasks.json', mode='r+') as fp:
        tasks = json.loads(await fp.read())
        for i, task in enumerate(tasks):
            if int(task['num_of_message']) == 4 and str(task['user_id']) == str(user_id):
                tasks.pop(i)
                break
        await fp.seek(0)
        await fp.truncate(0)
        await fp.write(json.dumps(tasks))
    await callback.answer()
    await create_task(callback.from_user.id, 5, str(datetime.datetime.now()+datetime.timedelta(days=1)))
    keyboard = aiogram.types.InlineKeyboardMarkup(2)
    keyboard.add(aiogram.types.InlineKeyboardButton('СЛЕДУЮЩИЙ УРОК➡️', callback_data='next_2'))
    keyboard.add(aiogram.types.InlineKeyboardButton('ЗАДАТЬ ВОПРОС ТРЕЙДЕРУ🤔', url='https://t.me/mhtrade_bo'))
    keyboard.add(aiogram.types.InlineKeyboardButton('TradingView📈', url='https://tradingview.com'))
    keyboard.add(aiogram.types.InlineKeyboardButton('Investing📰', url='https://investing.com'))
    await callback.message.answer_video('BAACAgIAAxkBAAMpZKq5loNVuQobRJr0e78QCYBGSCMAAu8yAAK-60lJVVxeHciv-6YvBA', caption=FORTH_MESSAGE, reply_markup=keyboard)

@dp.callback_query_handler(text='next_2')
async def next_2(callback: aiogram.types.CallbackQuery):
    user_id = callback.from_user.id
    async with aiofiles.open('tasks.json', mode='r+') as fp:
        tasks = json.loads(await fp.read())
        for i, task in enumerate(tasks):
            if int(task['num_of_message']) == 5 and str(task['user_id']) == str(user_id):
                tasks.pop(i)
                break
        await fp.seek(0)
        await fp.truncate(0)
        await fp.write(json.dumps(tasks))
    await callback.answer()
    await create_task(callback.from_user.id, 6, str(datetime.datetime.now()+datetime.timedelta(days=1)))
    keyboard = aiogram.types.InlineKeyboardMarkup(2)
    keyboard.add(aiogram.types.InlineKeyboardButton('СЛЕДУЮЩИЙ УРОК➡️', callback_data='next_3'))
    keyboard.add(aiogram.types.InlineKeyboardButton('ЗАДАТЬ ВОПРОС ТРЕЙДЕРУ🤔', url='https://t.me/mhtrade_bo'))
    await callback.message.answer_video('BAACAgIAAxkBAAMqZKq8aWu-QlwSLOezgl6Loxa8dycAAvIyAAK-60lJ_3ehS50JDoQvBA', caption=FIFTH_MESSAGE, reply_markup=keyboard)

@dp.callback_query_handler(text='next_3')
async def next_3(callback: aiogram.types.CallbackQuery):
    user_id = callback.from_user.id
    async with aiofiles.open('tasks.json', mode='r+') as fp:
        tasks = json.loads(await fp.read())
        for i, task in enumerate(tasks):
            if int(task['num_of_message']) == 6 and str(task['user_id']) == str(user_id):
                tasks.pop(i)
                break
        await fp.seek(0)
        await fp.truncate(0)
        await fp.write(json.dumps(tasks))
    await callback.answer()
    await create_task(callback.from_user.id, 7, str(datetime.datetime.now()+datetime.timedelta(days=1)))
    keyboard = aiogram.types.InlineKeyboardMarkup(2)
    keyboard.add(aiogram.types.InlineKeyboardButton('СЛЕДУЮЩИЙ УРОК➡️', callback_data='next_4'))
    keyboard.add(aiogram.types.InlineKeyboardButton('ПОЛУЧИТЬ ПОЛНЫЙ КУРС🔝', callback_data='next_4'))
    keyboard.add(aiogram.types.InlineKeyboardButton('ЗАДАТЬ ВОПРОС ТРЕЙДЕРУ🤔', url='https://t.me/mhtrade_bo'))
    await callback.message.answer_video('BAACAgIAAxkBAAMrZKq8clkDR1gAAV0AAfOsFde63pxtpQAC9DIAAr7rSUkNXaBYT_B3OC8E', caption=SIXTH_MESSAGE, reply_markup=keyboard)

@dp.callback_query_handler(text='next_4')
async def next_4(callback: aiogram.types.CallbackQuery):
    user_id = callback.from_user.id
    async with aiofiles.open('tasks.json', mode='r+') as fp:
        tasks = json.loads(await fp.read())
        for i, task in enumerate(tasks):
            if int(task['num_of_message']) == 7 and str(task['user_id']) == str(user_id):
                tasks.pop(i)
                break
        await fp.seek(0)
        await fp.truncate(0)
        await fp.write(json.dumps(tasks))
    await callback.answer()
    await create_task(callback.from_user.id, 8, str(datetime.datetime.now()+datetime.timedelta(days=1)))
    keyboard = aiogram.types.InlineKeyboardMarkup(2)
    keyboard.add(aiogram.types.InlineKeyboardButton('ПОЛУЧИТЬ ПОЛНУЮ ВЕРСИЮ КУРСА', callback_data='next_5'))
    keyboard.add(aiogram.types.InlineKeyboardButton('СТАТЬ УЧАСТНИКОМ КОМАНДЫ 🫂', callback_data='next_5'))
    keyboard.add(aiogram.types.InlineKeyboardButton('РЕЗУЛЬТАТЫ КОМАНДЫ📊', url='https://t.me/mh_stat'))
    keyboard.add(aiogram.types.InlineKeyboardButton('ЗАДАТЬ ВОПРОС ТРЕЙДЕРУ🤔', url='https://t.me/mhtrade_bo'))
    await callback.message.answer(SEVENTH_MESSAGE, reply_markup=keyboard)

@dp.callback_query_handler(text='next_5')
async def next_5(callback: aiogram.types.CallbackQuery):
    user_id = callback.from_user.id
    async with aiofiles.open('tasks.json', mode='r+') as fp:
        tasks = json.loads(await fp.read())
        for i, task in enumerate(tasks):
            if int(task['num_of_message']) == 8 and str(task['user_id']) == str(user_id):
                tasks.pop(i)
                break
        await fp.seek(0)
        await fp.truncate(0)
        await fp.write(json.dumps(tasks))
    await callback.answer()
    await create_task(callback.from_user.id, 10, str(datetime.datetime.now()+datetime.timedelta(days=1)))
    keyboard = aiogram.types.InlineKeyboardMarkup(2)
    keyboard.add(aiogram.types.InlineKeyboardButton('ПРИСОЕДИНИТЬСЯ К КОМАНДЕ👨🏻‍💻', callback_data='next_6'))
    await callback.message.answer(EIGHTH_MESSAGE, reply_markup=keyboard)

@dp.callback_query_handler(text='next_6')
async def next_6(callback: aiogram.types.CallbackQuery):
    await callback.message.answer(NINETH_MESSAGE)



async def create_task(user_id, num_of_message, date):
    tasks = []
    async with aiofiles.open('tasks.json', mode='r') as fp:
        tasks = json.loads(await fp.read())
        for i in tasks:
            if str(i['user_id']) == str(user_id) and int(num_of_message) == int(num_of_message) and datetime.datetime.strptime(i['date'], '%Y-%m-%d %H:%M:%S.%f') > datetime.datetime.now():
                return
        tasks.append({
            'user_id': user_id,
            'num_of_message': num_of_message,
            'date': date
        })
    async with aiofiles.open('tasks.json', mode='w') as fp:
        await fp.write(json.dumps(tasks))

async def sender():
    while True:
        tasks = []
        async with aiofiles.open('tasks.json', mode='r') as fp:
            tasks = json.loads(await fp.read())
        for i, task in enumerate(tasks):
            if datetime.datetime.strptime(task['date'], '%Y-%m-%d %H:%M:%S.%f') <= datetime.datetime.now():
                num_of_message = int(task["num_of_message"])
                user_id = task['user_id']
                tasks.pop(i)
                async with aiofiles.open('tasks.json', mode='w') as fp:
                    await fp.write(json.dumps(tasks))
                if num_of_message == 4:
                    await create_task(user_id, 5, str(datetime.datetime.now()+datetime.timedelta(days=1)))
                    keyboard = aiogram.types.InlineKeyboardMarkup(2)
                    keyboard.add(aiogram.types.InlineKeyboardButton('СЛЕДУЮЩИЙ УРОК➡️', callback_data='next_2'))
                    keyboard.add(aiogram.types.InlineKeyboardButton('ЗАДАТЬ ВОПРОС ТРЕЙДЕРУ🤔', url='https://t.me/mhtrade_bo'))
                    keyboard.add(aiogram.types.InlineKeyboardButton('TradingView📈', url='https://tradingview.com'))
                    keyboard.add(aiogram.types.InlineKeyboardButton('Investing📰', url='https://investing.com'))
                    await bot.send_video(user_id, 'BAACAgIAAxkBAAMpZKq5loNVuQobRJr0e78QCYBGSCMAAu8yAAK-60lJVVxeHciv-6YvBA', caption=FORTH_MESSAGE, reply_markup=keyboard)
                elif num_of_message == 5:
                    await create_task(user_id, 6, str(datetime.datetime.now()+datetime.timedelta(days=1)))
                    keyboard = aiogram.types.InlineKeyboardMarkup(2)
                    keyboard.add(aiogram.types.InlineKeyboardButton('СЛЕДУЮЩИЙ УРОК➡️', callback_data='next_3'))
                    keyboard.add(aiogram.types.InlineKeyboardButton('ЗАДАТЬ ВОПРОС ТРЕЙДЕРУ🤔', url='https://t.me/mhtrade_bo'))
                    await bot.send_video(user_id, 'BAACAgIAAxkBAAMqZKq8aWu-QlwSLOezgl6Loxa8dycAAvIyAAK-60lJ_3ehS50JDoQvBA', caption=FIFTH_MESSAGE, reply_markup=keyboard)
                elif num_of_message == 6:
                    await create_task(user_id, 7, str(datetime.datetime.now()+datetime.timedelta(days=1)))
                    keyboard = aiogram.types.InlineKeyboardMarkup(2)
                    keyboard.add(aiogram.types.InlineKeyboardButton('СЛЕДУЮЩИЙ УРОК➡️', callback_data='next_4'))
                    keyboard.add(aiogram.types.InlineKeyboardButton('ПОЛУЧИТЬ ПОЛНЫЙ КУРС🔝', callback_data='next_4'))
                    keyboard.add(aiogram.types.InlineKeyboardButton('ЗАДАТЬ ВОПРОС ТРЕЙДЕРУ🤔', url='https://t.me/mhtrade_bo'))
                    await bot.send_video(user_id, 'BAACAgIAAxkBAAMrZKq8clkDR1gAAV0AAfOsFde63pxtpQAC9DIAAr7rSUkNXaBYT_B3OC8E', caption=SIXTH_MESSAGE, reply_markup=keyboard)
                elif num_of_message == 7:
                    await create_task(user_id, 8, str(datetime.datetime.now()+datetime.timedelta(days=1)))
                    keyboard = aiogram.types.InlineKeyboardMarkup(2)
                    keyboard.add(aiogram.types.InlineKeyboardButton('ПОЛУЧИТЬ ПОЛНУЮ ВЕРСИЮ КУРСА', callback_data='next_5'))
                    keyboard.add(aiogram.types.InlineKeyboardButton('СТАТЬ УЧАСТНИКОМ КОМАНДЫ 🫂', callback_data='next_5'))
                    keyboard.add(aiogram.types.InlineKeyboardButton('РЕЗУЛЬТАТЫ КОМАНДЫ📊', url='https://t.me/mh_stat'))
                    keyboard.add(aiogram.types.InlineKeyboardButton('ЗАДАТЬ ВОПРОС ТРЕЙДЕРУ🤔', url='https://t.me/mhtrade_bo'))
                    await bot.send_message(user_id, SEVENTH_MESSAGE, reply_markup=keyboard)
                elif num_of_message == 8:
                    await create_task(user_id, 10, str(datetime.datetime.now()+datetime.timedelta(days=1)))
                    keyboard = aiogram.types.InlineKeyboardMarkup(2)
                    keyboard.add(aiogram.types.InlineKeyboardButton('ПРИСОЕДИНИТЬСЯ К КОМАНДЕ👨🏻‍💻', callback_data='next_6'))
                    await bot.send_message(user_id, EIGHTH_MESSAGE, reply_markup=keyboard)
                elif num_of_message == 10:
                    await create_task(user_id, 11, str(datetime.datetime.now()+datetime.timedelta(days=1)))
                    keyboard = aiogram.types.InlineKeyboardMarkup(2)
                    keyboard.add(aiogram.types.InlineKeyboardButton('УЧАСТВОВАТЬ В КОНКУРСАХ🎁', url='https://t.me/binarsignal'))
                    await bot.send_message(user_id, TENTH_MESSAGE, reply_markup=keyboard)
                elif num_of_message == 11:
                    keyboard = aiogram.types.InlineKeyboardMarkup(2)
                    keyboard.add(aiogram.types.InlineKeyboardButton('ПОЛУЧАТЬ РЕКОМЕНДАЦИИ📈', url='https://t.me/binarsignal'))
                    await bot.send_message(user_id, ELEVENTH_MESSAGE, reply_markup=keyboard)
        await asyncio.sleep(1)

async def on_start(_):
    asyncio.create_task(sender())

executor.start_polling(dp, on_startup=on_start)