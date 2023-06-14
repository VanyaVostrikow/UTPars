from SpecFunc.Users import User
from SpecFunc.Subscribe import Subscribe
from utparser import UTparser
import sqlite3
class Template:
    def _init_(self):
        pass
    async def list_subscribe(self, channels: dict=None):
        html_block = []
        conn = sqlite3.connect('DB/UTparser.sqlite3')
        cursor = conn.cursor()
        for i in range(len(channels)):
            channels[i] = channels[i][0][0]
            cursor.execute('SELECT Channel_id FROM Channels WHERE name_channel = ?', (channels[i],))
            url = cursor.fetchall()[0][0]
            url = '"https://www.youtube.com/' + url + '"'
            html_block.append("<a href=" + url + ">"+channels[i]+"</a>" + "\n")
        cursor.close()
        conn.close()
        text = 'Вы подписаны на каналы:\n\n'
        for i in range(len(html_block)):
            text = text + html_block[i]
        print(text)
        return text

