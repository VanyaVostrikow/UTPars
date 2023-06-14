import sqlite3

class User:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.conn = sqlite3.connect('DB/UTparser.sqlite3')
        self.cursor = self.conn.cursor()
    async def check_user(self):
        self.cursor.execute('SELECT * from users WHERE chat_id = ?', (self.chat_id, ))
        result = self.cursor.fetchall()
        if result == []:
            await User.create_user(self)
        else:
            self.cursor.close()
            self.conn.close()
    async def create_user(self):
        self.cursor.execute(f'INSERT INTO users (chat_id, subscribe) VALUES ({self.chat_id},TRUE);')
        self.conn.commit()
        self.cursor.close()
    async def get_user_id(self):
        self.cursor.execute('SELECT id FROM Users WHERE chat_id = ?', (self.chat_id, ))
        uid = self.cursor.fetchall()
        return uid
        