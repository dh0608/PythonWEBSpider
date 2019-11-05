# -*- coding: utf-8 -*-
import scrapy
import json
from wangzheimage.items import WangzheimageItem

"""
    案例：王者荣耀盒子英雄信息的爬取
并下载英雄图片
http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=9446162B3AEB79105F4B86E8951FE5B2&ovr=4.4.2&device=OPPO_OPPO+R11&net_type=1&client_id=sATctSUkHIiql%2FQN9piVmg%3D%3D&info_ms=%2Bjzrk%2FkHzKBMKCcdDR4kFQ%3D%3D&info_ma=gmv5GHk8N510tZTL4AB5z9AkYXtqpONOfNNfc30DAY4%3D&mno=0&info_la=WOTFRl5rVPGpG4HGPBPi%2Bw%3D%3D&info_ci=WOTFRl5rVPGpG4HGPBPi%2Bw%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=gmv5GHk8N510tZTL4AB5z9AkYXtqpONOfNNfc30DAY4%3D&os_level=19&os_id=54e1ad7860476621&resolution=720_1280&dpi=240&client_ip=192.168.11.185&pdunid=d786047662154e1a

"""


class Hero1Spider(scrapy.Spider):
    name = 'hero1'
    allowed_domains = ['gamehelper.gm825.com']
    start_urls = [
        'http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=9446162B3AEB79105F4B86E8951FE5B2&ovr=4.4.2&device=OPPO_OPPO+R11&net_type=1&client_id=sATctSUkHIiql%2FQN9piVmg%3D%3D&info_ms=%2Bjzrk%2FkHzKBMKCcdDR4kFQ%3D%3D&info_ma=gmv5GHk8N510tZTL4AB5z9AkYXtqpONOfNNfc30DAY4%3D&mno=0&info_la=WOTFRl5rVPGpG4HGPBPi%2Bw%3D%3D&info_ci=WOTFRl5rVPGpG4HGPBPi%2Bw%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=gmv5GHk8N510tZTL4AB5z9AkYXtqpONOfNNfc30DAY4%3D&os_level=19&os_id=54e1ad7860476621&resolution=720_1280&dpi=240&client_ip=192.168.11.185&pdunid=d786047662154e1a']

    def parse(self, response):
        data = json.loads(response.text)['list']
        a = len(data)
        print(f'共有{a}个英雄')
        for each in data:
            # print(each)
            name = each['name']
            print(f'英雄:{name}')

            img_url = each['cover']
            print(f'链接:{img_url}')

            ls = each['type']
            s = ('战士', '法师', '坦克', '刺客', '射手', '辅助')
            # print(ls)
            l = []
            for i in ls:
                # print(i)
                type = s[int(i)-1]
                l.append(type)
                print(f'英雄类型:{l}')
                item = WangzheimageItem(img_url=img_url, name=name)
                yield item

            print('='*130)


