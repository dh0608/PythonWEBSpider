# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

""" 
    人民网（scrapy）
    http://politics.people.com.cn/GB/1024/index1.html
    爬取新闻标题，链接，内容，发表时间
"""


class PeopleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    news_title = scrapy.Field()  # 新闻标题
    news_url = scrapy.Field()  # 新闻链接
    news_content = scrapy.Field()  # 内容
    pub_time = scrapy.Field()  # 发表时间
