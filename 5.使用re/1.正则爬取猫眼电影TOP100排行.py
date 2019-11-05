import json
import requests
from requests.exceptions import RequestException
import re
import time
import redis


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            '排名': item[0],
            '图片URL': item[1],
            '电影名称': item[2],
            '主演': item[3].strip()[3:],
            '上映时间': item[4].strip()[5:],
            '评分': item[5] + item[6]
        }


# 写入 txt中
def write_to_file(content):
    with open('TOP100.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


# 读取每个页面并存入txt
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

        # 存入 redis 数据库
        try:
            redis_con = redis.Redis(host="192.168.11.172", port=6379, db=0, decode_responses=True)
            """
                由于json.dumps 序列化时对中文默认使用的ascii编码.
                想输出真正的中文需要指定ensure_ascii=False： 
            """
            item = json.dumps(item, ensure_ascii=False)
            redis_con.lpush('maoyan', item)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # 分页一共有 10 页
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
