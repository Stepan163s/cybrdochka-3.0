import aiosqlite

async def create_tables():
    async with aiosqlite.connect('my_database.db') as db:
        cursor = await db.cursor()
        # Создаем таблицу "users"
        await cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                is_admin INTEGER,
                is_banned INTEGER
            )
        ''')
        # Создаем таблицу "images"
        await cursor.execute('''
            CREATE TABLE IF NOT EXISTS images (
                image_id INTEGER PRIMARY KEY,
                user_id INTEGER
            )
        ''')
        # Создаем таблицу "reactions"
        await cursor.execute('''
            CREATE TABLE IF NOT EXISTS reactions (
                reaction_id INTEGER PRIMARY KEY,
                image_id INTEGER,
                moon_reaction_count INTEGER DEFAULT 0,
                stone_face_reaction_count INTEGER DEFAULT 0,
                heart_reaction_count INTEGER DEFAULT 0
            )
        ''')
        await db.commit()
