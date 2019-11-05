# -*- coding: utf-8 -*-
import scrapy
import json
from douyuSpider.items import DouyuspiderItem


class Douyu1Spider(scrapy.Spider):
    name = 'douyu1'
    allowed_domains = ['capi.douyucdn.cn']
    start_urls = ['http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=']

    def __init__(self):
        # 初始化翻页
        self.offset = 0
        self.url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='

    def parse(self, response):
        # 将网页源码（json格式）序列化
        data = json.loads(response.text)['data']
        for each in data:
            item = DouyuspiderItem()
            # 昵称
            item['nickname'] = each['nickname']
            # 照片路径
            item['img_url'] = each['vertical_src']
            yield item

        # 进行翻页
        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)