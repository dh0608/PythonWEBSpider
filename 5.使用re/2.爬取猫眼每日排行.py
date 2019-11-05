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

if __name__ == '__main__':
    url = 'https://maoyan.com/board'
    html = get_one_page(url)
    # 拿到所有电影的 ul 标签
    patttern = r'<dd>.*?</dd>'
    pat_1 = re.findall(patttern, html, re.S | re.M)
    for item in pat_1:
        # print(item)
        # 匹配排名信息
        pattern1 = r'<dd>.*?board-index board-index-.*?>(.*?)</i>'
        ranking = re.search(pattern1, item, re.S | re.M).group(1)
        print('排名:', ranking)

        # 匹配电影的图片链接
        pattern2 = r'.*?<img data-src="(.*?) '
        img_url = re.search(pattern2, item, re.S | re.M).group(1)
        print('img_url:', img_url)

        # 电影名称
        pattern3 = r'.*?name.*?a.*?>(.*?)</a>'
        name = re.search(pattern3, item, re.S | re.M).group(1)
        print('电影名称:', name)

        # 主演
        pattern4 = r''


        # 上映时间


        # 评分








    time.sleep(1)