import aiosqlite
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from keyboard import admin_panel


async def SendPhotoChannel():
    print('photo')

async def SendTextChannel():
    print('photo')
          
async def no():
    print('photo')


async def SendPhotoModeration():
    print('moderation')

async def checkUser(user_id):
    async with aiosqlite.connect('my_database.db') as db:
        cursor = await db.cursor()
        await cursor.execute("SELECT username FROM users WHERE user_id=?", (user_id,))
        user_status = await cursor.fetchone()
    if user_status is None:
        return False  
    return bool(user_status[0])

async def getUsername(user_id):
    async with aiosqlite.connect('my_database.db') as db:
        cursor = await db.cursor()
        await cursor.execute("SELECT username FROM users WHERE user_id=?", (user_id,))
        username = await cursor.fetchone()  
    return str(username)

async def regUser(user_id):
    a = 1
    #message(' get your name ')
    #message(' sure ? ')
    #      buuton 
    # yes          no
    #if yes:
        #addUserDB(user_id)
    #else:
         #message(' get your name ')

async def addUserDB(user_id):
    print('hello')


async def welcom(message,user_id):
    name = await getUsername(user_id)
    await message.answer(f'{name}, добро пожаловать в бота !')



async def checkAdmin(user_id):
    async with aiosqlite.connect('my_database.db') as db:
        cursor = await db.cursor()
        await cursor.execute("SELECT is_admin FROM users WHERE user_id=?", (user_id,))
        adm_status = await cursor.fetchone()
    if adm_status is None:
        return False  
    return bool(adm_status[0])


async def PhotoModeration(photo_id, user_id):
    print('bimbim')
    #message(channel,photo)

async def SendPhotoChannel():
    print('bimbim')
    #message(channel,photo)

async def welcom_adm(message, user_id):
    name = await getUsername(user_id)
    await message.answer(f'Админ {name}, добро пожаловать в бота !',reply_markup = admin_panel)
