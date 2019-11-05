import requests
from bs4 import BeautifulSoup
import time
import random

"""   
案例：steam游戏爬虫（bs4）
https://store.steampowered.com/search/?os=win&filter=globaltopsellers
爬取游戏名称，链接，发布日期，价格，封面链接
"""


class StreamSpider:
    def __init__(self):
        self.url = "https://store.steampowered.com/search/?os=win&filter=globaltopsellers&page={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

    def get_bs4(self, url=None, page=1):
        response = requests.get(self.url.format(page), headers=self.headers)
        return BeautifulSoup(response.content, 'lxml')

    def get_game_detail(self, game):
        # 获取上传时间
        upload_time = game.select('div.col.search_released.responsive_secondrow')[0].text
        upload_time = upload_time.replace(",", "")
        print("upload_time:", upload_time)

        # 获取价格
        price = game.select('div.col.search_price.responsive_secondrow')[0].text
        price = price.strip()
        print("price:", price)
        # 获取游戏的链接
        game_url = game['href']
        print("game_url:", game_url)
        # 获取游戏的名称
        game_name = game.select('div.col.search_name.ellipsis > span')[0].string
        print("game_name:", game_name)

        print('='*120)

        with open('steamGame.txt', 'a', encoding="utf-8")as f:
            f.write(
                "game_name:" + game_name + "\t" + "game_url:" + game_url + "\tprice:" + price + "\tuploadTime:" + upload_time + "\n")

    def run(self):
        page = 1
        while page < 10:
            # 获取页面的tag对象
            soup = self.get_bs4(page=page)
            # 获取页面所有的游戏链接
            game_list = soup.select('div#search_resultsRows > a')
            for game in game_list:
                # 获取每个游戏的详情
                self.get_game_detail(game)
            page += 1


if __name__ == '__main__':
    StreamSpider().run()
