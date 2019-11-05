# -*- coding: utf-8 -*-
import scrapy
from people.items import PeopleItem
import time
import random as r


class News1Spider(scrapy.Spider):
    name = 'news1'
    allowed_domains = ['people.com.cn']
    start_urls = ['http://politics.people.com.cn/GB/1024/index1.html']

    def parse(self, response):
        # 提取每个新闻的信息
        news_ls = response.xpath('//div[contains(@class, "ej_list_box clear")]/ul/li')
        print(f'共有{len(news_ls)}个新闻')
        for new in news_ls:
            item = PeopleItem()
            # 新闻标题
            item['news_title'] = new.xpath('./a/text()').extract()[0].strip()

            # 新闻链接 http://politics.people.com.cn/n1/2019/0915/c1024-31353657.html
            top_url = 'http://politics.people.com.cn'
            item['news_url'] = top_url + new.xpath('./a/@href').extract()[0]

            # 发表时间
            item['pub_time'] = new.xpath('./em/text()').extract()[0].strip()
            # yield item
            # 打开每一个新闻链接进入详情页面
            req = scrapy.Request(item['news_url'], callback=self.parse_item)
            req.meta['item'] = item
            yield req
            time.sleep(r.random())

        # 翻页条件
        self.offset = 1
        if self.offset <= 7:
            self.offset += 1
            self.url = f'http://politics.people.com.cn/GB/1024/index{self.offset}.html'
            yield scrapy.Request(self.url, callback=self.parse)
            time.sleep(r.random())

    def parse_item(self, response):
        item = response.meta['item']
        # 内容
        item['news_content'] = response.xpath('//div[@id="rwb_zw"]//text()').extract()
        item['news_content'] = ''.join(item['news_content']).strip()
        print(item['news_content'])
        yield item
