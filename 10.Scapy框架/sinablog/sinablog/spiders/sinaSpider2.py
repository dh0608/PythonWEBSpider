# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from sinablog.items import SinablogItem


class Sinaspider2Spider(CrawlSpider):
    name = 'sinaSpider2'
    allowed_domains = ['blog.sina.com.cn']
    # 博客主页
    start_urls = ['http://blog.sina.com.cn/s/articlelist_1525875683_0_1.html']

    # 内容详情页链接
    content_url = LinkExtractor(restrict_xpaths=('//span[@class="atc_title"]/a',))
    # 翻页链接
    page_url = LinkExtractor(restrict_xpaths=('//li[@class="SG_pgnext"]/a',))
    rules = [
        Rule(content_url, callback='parse_item'),
        Rule(page_url, follow=True)
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
