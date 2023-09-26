import aiosqlite
import asyncio
import logging
import sys
from typing import Any, Dict
from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

from function import checkUser, welcom, regUser, checkAdmin, welcom_adm, SendPhotoChannel, SendTextChannel, no

bot = Bot(token='env.tokem')
dp = Dispatcher()



@dp.message(F.text == '/start')                #обработка команды /start
async def start(message: Message):
    user_id = message.from_user.id             #получаем user_id -> int:
    result = await checkUser(user_id)          #проверяем есть ли юзер в базе данных checkUser(user_id) -> bool:
    if result:
        adm = checkAdmin(user_id)              #проверяем админ ли юзер checkAdmin(user_id) -> bool:
        if adm:
            await welcom_adm(message, user_id) #отправляем приветсвенное сообщение админу
        else:
            await welcom(message,user_id)      #отправляем приветсвенное сообщение пользователю
    else:
        await regUser(user_id)                 #добавляем пользователя в базу данных
    

@dp.message(F.text)                            #обработка текста
async def start(message: Message):
    user_id = message.from_user.id             #получаем user_id -> int:
    result = await checkUser(user_id)          #проверяем есть ли юзер в базе данных checkUser(user_id) -> bool:
    if result:
        adm = checkAdmin(user_id)              #проверяем админ ли юзер checkAdmin(user_id) -> bool:
        if adm:
            await SendTextChannel(message) #отправляем приветсвенное сообщение админу
        else:
            await no(message,user_id)          #отправляем сообщение что не понимаем пользователя




@dp.message(F.photo)                           #обработка фото
async def photo(message: Message):
    user_id = message.from_user.id             #получаем user_id -> int:
    result = await checkUser(user_id)          #проверяем есть ли юзер в базе данных checkUser(user_id) -> bool:
    if result:
        adm = checkAdmin(user_id)              #проверяем админ ли юзер checkAdmin(user_id) -> bool:
        if adm:
            await welcom_adm(message, user_id) #отправляем приветсвенное сообщение админу
        else:
            await welcom(message, user_id)     #отправляем приветсвенное сообщение пользователю
    else:
        await regUser(user_id)                 #добавляем пользователя в базу данных


@dp.message(F.video)                           #обработка видео
async def video(message: Message):
    user_id = message.from_user.id             #получаем user_id -> int:
    result = await checkUser(user_id)          #проверяем есть ли юзер в базе данных checkUser(user_id) -> bool:
    if result:
        adm = checkAdmin(user_id)              #проверяем админ ли юзер checkAdmin(user_id) -> bool:
        if adm:
            await welcom_adm(message, user_id) #отправляем приветсвенное сообщение админу
        else:
            await welcom(message, user_id)     #отправляем приветсвенное сообщение пользователю
    else:
        await regUser(user_id)                 #добавляем пользователя в базу данных





async def main():
    await dp.start_polling(bot)



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')












