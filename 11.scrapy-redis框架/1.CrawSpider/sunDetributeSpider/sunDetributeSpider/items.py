# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SundetributespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 编号
    id = scrapy.Field()

    # 标题
    title = scrapy.Field()

    # 链接
    title_url = scrapy.Field()

    # 内容
    content = scrapy.Field()

    # 投诉者
    complainant = scrapy.Field()

    # 投诉时间
    complain_time = scrapy.Field()
