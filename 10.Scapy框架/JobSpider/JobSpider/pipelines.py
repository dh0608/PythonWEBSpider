# -*- coding: utf-8 -*-
import codecs
import csv
import pymysql
import os


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class JobspiderPipeline(object):
    def __init__(self):
        # 保存的文件名
        self.filename = codecs.open('51job.csv', 'w', encoding='utf-8')
        # 将数据写入文件中
        self.wr = csv.writer(self.filename, dialect='excel')
        # 写入数据
        self.wr.writerow(['name', 'corp', 'city', 'salary', 'pub_date'])

    def process_item(self, item, spider):
        self.wr.writerow(['职位名称:' + item['name'] + '\n'
                          '公司名称:' + item['corp'] + '\n'
                          '城市:' + item['city'] + '\n'
                          '薪水:' + item['salary'] + '\n'
                          '发布日期:' + item['pub_date'] + '\n'])
        return item

    def close_spider(self, spider):
        # 关闭文件
        self.filename.close()


class JobspiderDbPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.0.105', port=3306, user='root', password='root', db='dbjob51',
                                    charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        spider.log('csv path:' + os.path.abspath('./'))
        strsql = "insert into tbjob VALUES(%s,%s,%s,%s,%s)"
        parmas = [item['name'], item['corp'], item['pub_date'], item['city'], item['salary']]
        self.cur.execute(strsql, parmas)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
