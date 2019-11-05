# -*- coding: utf-8 -*-
import scrapy
from bilibili.items import BilibiliItem
import time
import random as r

class BilitopSpider(scrapy.Spider):
    name = 'biliTop'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking#!/all/0/0/7/']

    def parse(self, response):
        # 获得每个排名的标签
        ls = response.xpath('//div[@class="rank-list-wrap"]/ul/li')
        print(f'{len(ls)}')
        for each in ls:
            item = BilibiliItem()
            # 编号
            item['id'] = each.xpath('.//div[@class="num"]/text()').extract()[0].strip()

            # 标题
            item['title'] = each.xpath('.//div[@class="info"]/a/text()').extract()[0].strip()

            # 链接 https://www.bilibili.com/video/av67439251/
            item['title_url'] = 'https:' + each.xpath('.//div[@class="info"]/a/@href').extract()[0]

            # 作者
            item['author'] = each.xpath('.//div[@class="detail"]/a/span/text()').extract()[0].strip()

            # 综合评分
            item['total_score'] = each.xpath('.//div[@class="pts"]/div/text()').extract()[0].strip()

            # 播放量
            item['vv'] = each.xpath('.//div[@class="detail"]/span[1]/text()').extract()[0].strip()

            # 评论数
            item['comments'] = each.xpath('.//div[@class="detail"]/span[2]/text()').extract()[0].strip()

            yield item
            time.sleep(r.random())