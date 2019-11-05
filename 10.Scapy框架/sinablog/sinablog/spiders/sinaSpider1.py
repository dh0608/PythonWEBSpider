# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from sinablog.items import SinablogItem

"""
    sina 博客爬虫（CrawlSpider）
    http://blog.sina.com.cn/s/articlelist_1525875683_0_1.html
    爬取博客标题，url
"""


class Sinaspider1Spider(CrawlSpider):
    name = 'sinaSpider1'
    allowed_domains = ['blog.sina.com.cn']
    # 第一篇博客详情页面
    start_urls = ['http://blog.sina.com.cn/s/blog_5af303e30102yff6.html']

    rules = [
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="articalfrontback SG_j_linedot1 clearfix"]/div/a',)), callback='parse_item'
             , follow=True)
    ]

    def parse_item(self, response):
        blog_url = response.url
        title = response.xpath('//h2[@class="titName SG_txta"]/text()').extract()
        if len(title) > 0:
            title = title[0]
        else:
            title = '空'
        content = response.xpath('//div[@id="sina_keyword_ad_area2"]//text()').extract()
        if len(content) > 0:
            content = ''.join(content).strip()
        else:
            content = '空'

        item = SinablogItem(blog_url=blog_url, title=title, content=content)
        yield item

    # def parse(self, response):
    #     pass
