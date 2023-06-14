import sqlite3
from utparser import UTparser
from SpecFunc.Users import User
class Subscribe:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.conn = sqlite3.connect('DB/UTparser.sqlite3')
        self.cursor = self.conn.cursor()
    async def get_list(self):
        self.cursor.execute('SELECT * FROM Users WHERE chat_id=?', (self.chat_id, ))
        user_id = self.cursor.fetchall()[0][0]
        self.cursor.execute('SELECT channel_id FROM Subscribe WHERE user_id = ?', (user_id, ))
        channel_id = self.cursor.fetchall()
        channels = []
        print(1)
        for i in range(len(channel_id)):
            self.cursor.execute('SELECT name_channel FROM Channels WHERE id =?', (channel_id[i]))
            channels.append(self.cursor.fetchall())
        print(channels)
        self.cursor.close()
        self.conn.close()
        return channels
    async def add_chanell(self, link:str=None):
        self.cursor.execute(f'SELECT * FROM Channels WHERE Channel_id=?', (link,))
        print(1)
        channel_id_list = self.cursor.fetchall()
        if channel_id_list == []:
            print("add")
            path = UTparser().channel_id_to_logo(link)
            name = UTparser().get_channel_name(link)
            self.cursor.execute(f'INSERT INTO Channels (channel_id, name_channel, logo) VALUES (?, ?, ?);', (link, name, path,))
            self.conn.commit()
        else:
            print("notadd")
            channel_id = channel_id_list[0][0]
            self.cursor.execute('SELECT id FROM Users WHERE chat_id=?', (self.chat_id,))
            id = self.cursor.fetchall()[0][0]
            self.cursor.execute('SELECT channel_id FROM Subscribe WHERE user_id=? AND channel_id=?', (id, channel_id, ))
            result = self.cursor.fetchall()
            if result == []:
                print(4)
                pass
            else:
                print(5)
                error = True
                return error
        await Subscribe(self.chat_id).subscribe_user_to_channel(link=link)
    async def subscribe_user_to_channel(self, link):
        print('subscribe')
        self.cursor.execute('SELECT id from Channels WHERE channel_id = ?', (link, ))
        channel_id = self.cursor.fetchall()[0][0]
        self.cursor.execute('SELECT id FROM users WHERE chat_id = ?', (self.chat_id, ) )
        user_id = self.cursor.fetchall()[0][0]
        self.cursor.execute('INSERT INTO Subscribe (user_id, channel_id, timeline) VALUES (?, ?, ?)', (user_id, str(channel_id), '0',))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
    async def __get_channel_id(self, link):
        self.cursor.execute('SELECT id FROM Channels Where channel_id = ?', (link, ))
        cid = self.cursor.fetchall()
        return cid
    async def __check_sub(self, link,):
        cid = await Subscribe(self.chat_id).__get_channel_id(link)
        uid = await User(self.chat_id).get_user_id()
        uid = uid[0][0]
        cid = cid[0][0]
        print(cid, uid)
        self.cursor.execute('SELECT * FROM Subscribe WHERE channel_id = ? AND user_id = ?', (cid, uid, ))
        result = self.cursor.fetchall()
        if result == []:
            return False
        else:
            return True
    async def unsub_from_channel(self, link):
        print('delete')
        sub = await Subscribe(self.chat_id).__check_sub(link)
        
        print(sub)
        cid = await Subscribe(self.chat_id).__get_channel_id(link)
        cid = cid[0][0]
        print(cid)
        uid = await User(self.chat_id).get_user_id()
        uid = uid[0][0]
        print(uid)
        if sub == True:
            self.cursor.execute('DELETE FROM Subscribe WHERE user_id = ? AND channel_id = ?', (uid, cid,))
            self.conn.commit()
            return True
        else:
            print("NONE")
            return False
