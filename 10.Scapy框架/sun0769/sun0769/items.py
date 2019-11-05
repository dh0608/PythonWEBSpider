# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
    阳光热线问政平台（spider）
    http://wz.sun0769.com/index.php/question/questionType?type=4&page=
    爬取投诉帖子的标题，编号，链接，内容，投诉者，投诉时间
    存储到mysql数据库
"""


class Sun0769Item(scrapy.Item):
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
