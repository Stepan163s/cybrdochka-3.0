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

from function import checkUser, getUsername, welcom, regUser, checkAdmin

bot = Bot(token='env.tokem')
dp = Dispatcher()


# обработка команды /start
@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    user_id = message.from_user.id
    result = await checkUser(user_id)          #проверяем есть ли юзер в базе данных checkUser() -> bool:
    if result:
        adm = checkAdmin(user_id)  #проверяем админ ли юзер checkAdmin() -> bool:
        name = await getUsername(user_id)
        await welcom(message, name)
    else:
        await regUser(user_id)
    
#обработка фото
@dp.message(F.photo)
async def eho_photo(message: Message):
    user_id = message.from_user.id             #получаем user_id -> int:
    result = await checkUser(user_id)          #проверяем есть ли юзер в базе данных checkUser(user_id) -> bool:



async def main():
    await dp.start_polling(bot)



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
