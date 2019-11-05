# -*- coding: utf-8 -*-
import pymysql


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BilibiliPipeline(object):
    def __init__(self):
        try:
            # 获取数据库的链接
            self.con = pymysql.connect(host='localhost', port=3306, db='bilibili', user='root', password='root',
                                       charset='utf8')
            # 创建游标
            self.cur = self.con.cursor()
        except Exception as e:
            print(f'连接错误{e}')

    def process_item(self, item, spider):
        try:
            # 向数据库插入数据
            sql = 'insert into top100(id, title, title_url, author, total_score, vv, comments) values (%s,%s,%s,%s,%s,%s,%s)'
            params = [item['id'], item['title'], item['title_url'], item['author'], item['total_score'], item['vv'],
                      item['comments']]
            # 执行 sql
            self.cur.execute(sql, params)
            # 提交
            self.con.commit()

        except Exception as e:
            print(f'连接错误{e}')

        return item

    def close_spider(self, spider):
        # 关闭游标
        self.cur.close()
        # 关闭数据库
        self.con.close()
