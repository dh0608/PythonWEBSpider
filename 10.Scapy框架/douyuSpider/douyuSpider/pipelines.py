# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import os


class DouyuspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class DouyuImagePipeline(ImagesPipeline):
    # 获取图片的位置
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        img_url = item['img_url']
        yield scrapy.Request(img_url)

    def item_completed(self, results, item, info):
        # 固定写法，获取图片路径，同时判断这个路径是否正确，
        # 如果正确，就放到 img_path 里， ImagesPipeline 源码剖析可见
        print('item_completed:', info)
        if results[0][0] == True:
            # 图片路径
            img_path = results[0][1]["path"]
        print("2:", img_path)
        pri_name = self.IMAGES_STORE + "/" + img_path
        fin_name = self.IMAGES_STORE + "/" + item["nickname"] + ".jpg"
        os.rename(pri_name, fin_name)
        item["img_path"] = self.IMAGES_STORE + "/" + item["nickname"]
        return item
