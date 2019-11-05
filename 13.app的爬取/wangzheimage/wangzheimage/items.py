# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangzheimageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 昵称
    img_url = scrapy.Field()  # 图片路径
    img_path = scrapy.Field()  # 照片本地存储位置
