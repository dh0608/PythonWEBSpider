# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
    案例：斗鱼主播照片爬虫
    http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=
    主播昵称、照片路径、本地存储位置、
"""


class DouyuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nickname = scrapy.Field()  # 昵称
    img_url = scrapy.Field()  # 图片路径
    img_path = scrapy.Field()  # 照片本地存储位置
