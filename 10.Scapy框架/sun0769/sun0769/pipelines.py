# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Sun0769Pipeline(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='localhost', port=3306, db='ygrx', user='root', password='root',
                                        charset='utf8')
            self.cur = self.conn.cursor()
        except Exception as e:
            print('conn error...', e)

    def process_item(self, item, spider):
        try:
            strsql = 'insert into question(id, title, title_url, content, complainant, complain_time) VALUES (%s,%s,%s,%s,%s,%s)'
            params = [item['id'], item['title'], item['title_url'], item['content'], item['complainant'],
                      item['complain_time']]
            self.cur.execute(strsql, params)
            self.conn.commit()
        except Exception as e:
            print('insert error...', e)

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
