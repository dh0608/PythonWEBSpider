import requests
import random
import time
import os

url = 'https://aweme-eagle-hl.snssdk.com/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=0&count=6&volume=0.7333333333333333&pull_type=3&need_relieve_aweme=0&filter_warn=0&req_from&is_cold_start=0&longitude=104.562752&latitude=31.534006&address_book_access=1&gps_access=1&ts=1569845053&js_sdk_version=&app_type=normal&openudid=f48e38e9cb7b7993&version_name=6.5.0&device_type=SM-G955N&ssmix=a&iid=86823487947&os_api=19&mcc_mnc=46007&device_id=68871435919&resolution=1280*720&device_brand=samsung&aid=1128&manifest_version_code=650&app_name=aweme&_rticket=1569845053205&os_version=4.4.2&device_platform=android&version_code=650&update_version_code=6502&ac=wifi&dpi=240&uuid=863064010244145&language=zh&channel=aweGW'
headers = {
    'Accept-Encoding': 'gzip',
    'X-SS-REQ-TICKET': '1569845053199',
    'sdk-version': '1',
    'Cookie': 'install_id=86823487947; ttreq=1$46957e5eeafd6a6405fffdd7f15a0221b7a207f9; odin_tt=e30a629c22ca65ddbdc1a253981a5453b948e20436043738573b425433b2f008e037110936f95fb0a524ae7fa46385ef646391d29425d0db39b7a2f5678d495a',
    'x-tt-token': '00c1cbf49f0c33619c763d31da80535a4ecb32e438a13b631ef37d3e59d4a2b5b93b10b63ca4c04f2f18f951cf728226b05a',
    'X-Gorgon': '03006cc04400cc0351758d0933fe67749d5bbe40cc27103d4eb8',
    'X-Khronos': '1569845053',
    'Host': 'aweme-eagle-hl.snssdk.com',
    'Connection': 'Keep-Alive',
    'User-Agent': 'okhttp/3.10.0.1'
}
headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
proxies = {
    # "http": "http://10.10.1.10:3128",
    "http": "183.166.70.227:9999",
}
requests.packages.urllib3.disable_warnings()
r = requests.get(url, headers=headers, verify=False, proxies=proxies).json()
# print(r)
for i in r['aweme_list']:
    # print(i)
    # 视频描述
    desc = i['desc']
    print(f'desc:{desc}')
    # 视频路径
    url1 = i['video']['play_addr_lowbr']['url_list'][0]
    print(f'url1:{url1}')
    print('=' * 130)
    time.sleep(random.random())
    if not os.path.exists('./videos'):
        os.mkdir('./videos')
    # with open(f'./videos/{index}.mp4', 'wb') as f:
    #     r1 = requests.get(url, headers=headers1)

    # r = requests.get(url, stream=True)
    r1 = requests.get(url1, stream=True)
    with r1 as r:
        chunk_size = 1024
        content_size = int(r.headers['content-length'])
        print('下载开始......')
        with open(f'./videos/{desc}.mp4', "wb") as f:
            n = 1
            for chunk in r1.iter_content(chunk_size=chunk_size):
                loaded = n * 1024.0 / content_size
                f.write(chunk)
                print(f'已下载{loaded:%}')
                n += 1
    print('下载结束.....')



