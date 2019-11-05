# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.utils.project import get_project_settings
from wangzheimage import settings
import os


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class WangzheimagePipeline(ImagesPipeline):
    # 获取图片的位置
    if not os.path.exists('./images'):
        os.mkdir('./images')
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        img_url = item['img_url']
        yield scrapy.Request(img_url)

    # def file_path(self, request, response=None, info=None):
    #     # 这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
    #     path = super(WangzheimagePipeline, self).file_path(request, response, info)
    #     # 英雄名
    #     name = request.item.get('name')
    #
    #     images_store = settings.IMAGES_STORE
    #     if not os.path.exists(images_store):
    #         os.mkdir(images_store)
    #     image_name = path.replace("full/", f"{name}")
    #     image_path = os.path.join(images_store, image_name)
    #     return image_path

    def item_completed(self, results, item, info):
        print('results', results)
        print('info', info)
        if results[0][0] == True:
            # 原始照片路径
            img_path = self.IMAGES_STORE + '/' +results[0][1]['path']
            new_path = self.IMAGES_STORE + '/' + item['name'] + '.jpg'
            os.rename(img_path, new_path)
            item['img_path'] = new_path
            return item