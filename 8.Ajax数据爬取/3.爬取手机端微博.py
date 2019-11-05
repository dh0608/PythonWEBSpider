import requests
from urllib.parse import urlencode

# Request URL: https://multimedia.api.weibo.com/2/multimedia/user/play_history/report.json?source=2637646381&play_type=0&video_orientation=vertical&video_duration=11.19&id=4387045768207049&id_type=0&seconds=0&oid=1034:4387045695535031&reqHost=https://weibo.com/u/5134857819?is_all=1
base_url = 'https://multimedia.api.weibo.com/2/multimedia/user/play_history/report.json?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://weibo.com/u/5134857819?is_all=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def get_pages(page):
    params = {

        'reqHost': 'https://m.weibo.cn/u/5134857819',
    }

    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json(), page
    except requests.ConnectionError as e:
        print('Error', e.args)




