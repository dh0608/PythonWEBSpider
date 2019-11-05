# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()   # 职位名称
    corp = scrapy.Field()   # 公司名称
    city = scrapy.Field()   # 工作城市
    salary = scrapy.Field()  # 薪资待遇
    pub_date = scrapy.Field()   # 招聘信息发布时间
