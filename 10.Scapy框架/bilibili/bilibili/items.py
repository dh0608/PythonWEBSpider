# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
    b站排行榜爬虫（scrapy）
    https://www.bilibili.com/ranking#!/all/0/0/7/
    爬取编号，标题，url，综合评分，播放量，评论数
    存储到mysql数据库
"""


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()  # 编号
    title = scrapy.Field()  # 标题
    title_url = scrapy.Field()  # 链接
    author = scrapy.Field()  # 作者
    total_score = scrapy.Field()    # 综合评分
    vv = scrapy.Field()  # 播放量
    comments = scrapy.Field()  # 评论数
