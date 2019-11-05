import requests
import json
import random
import time

# http://zjj.zhuzhou.gov.cn/c13948/
url = 'http://zjj.zhuzhou.gov.cn/fcjadpater/select/WWW_YSXK_002'
head = {}
head[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
PIC_SERVER_PREFIX = "http://218.75.204.3:5636"

for page in range(1, 10):
    print('page:', page)
    params = {
        'pageIndex': page,
        'pageSize': 15
    }
    response = requests.post(url, headers=head, params=params)
    data = json.loads(response.json()['rows'])
    print(len(data))

    for item in data:
        bid = item['bid']
        cdno = item['cdno']
        fpath = item['fpath']
        lname = item['lname']
        pid = item['pid']
        pname = item['pname']
        img_url = PIC_SERVER_PREFIX + fpath
        print('bid:', bid)
        print('cdno:', cdno)
        print('fpath:', fpath)
        print('lname:', lname)
        print('pid:', pid)
        print('pname:', pname)
        print('img_url:', img_url)
        print('=' * 60)

        img = requests.get(img_url, headers=head).content
        img_path = './images/ysz/' + cdno + '.jpg'
        with open(img_path, 'wb') as file:
            file.write(img)
    time.sleep(random.random())
