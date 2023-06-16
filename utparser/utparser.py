import requests
from telebot.SpecFunc.doubler_killer import doubler_killer
from bs4 import BeautifulSoup
import re
class UTparser:
    def __init__(self):
        self.domain = 'https://www.youtube.com/'
        self.soup_watch = 'watch?v='
        self.img_url = 'http://i4.ytimg.com/vi/'
    def getting_url(self, channel_id, video_id):
        url = self.domain + self.soup_watch + video_id
        return url
    def channel_id_to_video_url(self, channel_id:str=None):
        print(1)
        req = requests.get(self.__domain + channel_id + '/videos')
        print(2)
        send = BeautifulSoup(req.text, "html.parser")
        print(3)
        search = send.find_all("script")
        print(4)
        key = '"videoId":"'
        print(5)
        video_soup = re.findall(key + r"([^*]{11})", str(search))
        print(6)
        video_soup = doubler_killer(video_soup)
        print(7)
        video_soup = video_soup[:2]
        print(8)
        print(video_soup)
        return video_soup
    def get_channel_name(self, link):
        url = self.domain + link
        content = requests.get(url)
        soup = BeautifulSoup(content.text, "html.parser")
        json = soup.find('title')
        json = str(json)
        json=json.replace('<title>', '')
        json=json.replace('</title>', '')
        chanell_name = json.rstrip('- YouTube')
        print(chanell_name)
        return chanell_name
    def video_id_to_thumbnail(self, video_id: str=None):
        url = self.__img_url + video_id + '/maxresdefault.jpg'
        p = requests.get(url)
        path = f"img/thumbnails/{video_id}.jpg"
        out = open(path, "wb")
        out.write(p.content)
        out.close()
        print('pass')
        return path
    def scrape_video_count(self, video_id):
        content = requests.get(self.domain + self.soup_watch+video_id)
        soup = BeautifulSoup(content.text, "html.parser")
        view_count = soup.find('meta', {'itemprop': 'interactionCount'}).get('content')
        return view_count
    def scrape_video_date(self, link):
        content = requests.get(self.domain+self.soup_watch + link)
        soup = BeautifulSoup(content.text, "html.parser")
        view_count = soup.find('meta', {'itemprop': 'uploadDate'}).get('content')
        return view_count
    def scrape_videoname(self, video_id):
        dir = {}
        for i in range(len(video_id)):
            url = self.domain + self.soup_watch + video_id[i]
            content = requests.get(url)

            soup = BeautifulSoup(content.text, "html.parser")
            json = soup.find('title')
            json = str(json)
            json=json.replace('<title>', '')
            json=json.replace('</title>', '')
            json = json.rstrip('- YouTube')
            #video_name = (soup.find('meta', {'itemprop': 'interactionCount'}).get('content'))
            dir.update({url:json})
        print(dir)
        return dir
    def channel_id_to_logo(self, channel_id:str=None):
        print(1)
        url = str(UTparser().domain) + str(channel_id) + '/videos'
        req = requests.get(url)
        print(2)
        send = BeautifulSoup(req.text, "html.parser")
        print(3)
        search = send.find_all("script")
        print(4)
        key = 'yt3'
        print()
        video_soup = re.findall(key + r"([^*]{100})", str(search))
        print(6)
        video_soup = doubler_killer(video_soup)
        print(7)
        print(video_soup)
        video_soup = video_soup[0][:-1]
        print(video_soup)
        video_soup = str(video_soup).replace('s48', 's500')
        print(video_soup)
        url = 'https://yt3' + video_soup
        print(url)
        p = requests.get(url)
        path = f"img/logo/{channel_id}.jpg"
        print(path)
        out = open(path, "wb")
        out.write(p.content)
        out.close()
        return path
