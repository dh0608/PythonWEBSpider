"""
    案例：王者荣耀盒子热点新闻爬虫
    爬取热点新闻信息
    http://gamehelper.gm825.com/wzry/hot/information?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=9446162B3AEB79105F4B86E8951FE5B2&ovr=4.4.2&device=OPPO_OPPO+R11&net_type=1&client_id=sATctSUkHIiql%2FQN9piVmg%3D%3D&info_ms=%2Bjzrk%2FkHzKBMKCcdDR4kFQ%3D%3D&info_ma=gmv5GHk8N510tZTL4AB5z9AkYXtqpONOfNNfc30DAY4%3D&mno=0&info_la=WOTFRl5rVPGpG4HGPBPi%2Bw%3D%3D&info_ci=WOTFRl5rVPGpG4HGPBPi%2Bw%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=gmv5GHk8N510tZTL4AB5z9AkYXtqpONOfNNfc30DAY4%3D&os_level=19&os_id=54e1ad7860476621&resolution=720_1280&dpi=240&client_ip=192.168.11.185&pdunid=d786047662154e1a
    http://gamehelper.gm825.com/wzry/news/list?pn=2&channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=9446162B3AEB79105F4B86E8951FE5B2&ovr=4.4.2&device=OPPO_OPPO+R11&net_type=1&client_id=sATctSUkHIiql%2FQN9piVmg%3D%3D&info_ms=%2Bjzrk%2FkHzKBMKCcdDR4kFQ%3D%3D&info_ma=gmv5GHk8N510tZTL4AB5z9AkYXtqpONOfNNfc30DAY4%3D&mno=0&info_la=WOTFRl5rVPGpG4HGPBPi%2Bw%3D%3D&info_ci=WOTFRl5rVPGpG4HGPBPi%2Bw%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=gmv5GHk8N510tZTL4AB5z9AkYXtqpONOfNNfc30DAY4%3D&os_level=19&os_id=54e1ad7860476621&resolution=720_1280&dpi=240&client_ip=192.168.11.185&pdunid=d786047662154e1a
    User-Agent: Dalvik/1.6.0 (Linux; U; Android 4.4.2; OPPO R11 Build/NMF26X)
"""
import requests
import time

# 默认页数为1
pn = 1
headers = {
    'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; OPPO R11 Build/NMF26X)'
}

# 根据分析 url 的规则发现只有 pn（页码）在变
# 构造 url 爬取前4页信息
for pn in range(1, 5):
    url = 'http://gamehelper.gm825.com/wzry/news/list?' + str(pn) \
          + '&channel_id=90009a&app_id=h9044j&game_id=7622&game_' \
            'name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0' \
            '&version_code=13010&cuid=9446162B3AEB79105F4B86E8951FE5B2' \
            '&ovr=4.4.2&device=OPPO_OPPO+R11&net_type=1' \
            '&client_id=sATctSUkHIiql%2FQN9piVmg%3D%3D&info_ms=%2Bjzrk%2FkHzKBMKCcdDR4kFQ%3D%3D' \
            '&info_ma=gmv5GHk8N510tZTL4AB5z9AkYXtqpONOfNNfc30DAY4%3D' \
            '&mno=0&info_la=WOTFRl5rVPGpG4HGPBPi%2Bw%3D%3D&info_ci=WOTFRl5rVPGpG4HGPBPi%2Bw%3D%3D' \
            '&mcc=0&clientversion=13.0.1.0&bssid=gmv5GHk8N510tZTL4AB5z9AkYXtqpONOfNNfc30DAY4%3D' \
            '&os_level=19&os_id=54e1ad7860476621&resolution=720_1280&dpi=240' \
            '&client_ip=192.168.11.185&pdunid=d786047662154e1a'
    r = requests.get(url, headers=headers).json()
    print(f'--------------------------第{pn}页-----------------------------------')
    # print(r)
    # 新闻列表
    ls = r['list']
    for new in ls:
        # print(new)
        news_title = new['title']
        print(f'标题:{news_title}')

        keyword = new['keyword_name']
        print(f'关键字:{keyword}')

        tags_name =new['tags_name']
        print(f'分类:{tags_name}')

        description = new['description']
        print(f'详情:{description}')

        img_url = new['cover']
        print(f'图片地址:{img_url}')

        ctime = new['ctime']
        time_Array = time.localtime(int(ctime))
        pub_time = time.strftime("%Y-%m-%d %H:%M:%S", time_Array)
        print(f'发布时间:{pub_time}')

        print('='*130)