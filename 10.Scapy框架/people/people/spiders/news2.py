# -*- coding: utf-8 -*-
import scrapy


class News2Spider(scrapy.Spider):
    name = 'news2'
    allowed_domains = ['people.com.cn']
    start_urls = ['http://people.com.cn/']

    def parse(self, response):
        pass
