import requests
from lxml import html
import pymysql
import time
import random
import re

etree = html.etree

"""
    案例：链家二手房
    https://sh.lianjia.com/ershoufang/
    提取标题，链接，单价，总价，基本信息，房源特色信息
    保存到mysql数据库
"""

"""
    1.爬取网页
"""
url = 'https://sh.lianjia.com/ershoufang/'
start_page = int(input('请输入起始的页码：'))
end_page = int(input('请输入结束的页码：'))
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}

for page in range(start_page, end_page + 1):
    pg = 'pg' + str(page)
    params = {
        'kw': pg
    }
    r = requests.get(url, params=params, headers=headers)
    html = r.content
    # print(html)

    """
        2.获取网页数据
    """
    # 将 html 字符串解析为 html 文档
    html = etree.HTML(html)
    # 获取房子信息对应的 li 标签
    ls = html.xpath('.//li[contains(@class,"clear LOGVIEWDATA LOGCLICKDATA")]')
    print('len', len(ls))
    # 拿到标签下对应的数据
    for item in ls:
        # 标题
        title = item.xpath('.//div[@class="info clear"]/div/a/text()')[0]
        print('标题：', title)
        # 链接
        title_url = item.xpath('.//div[@class="info clear"]/div/a/@href')[0]
        print('链接：', title_url)
        # 单价
        unitPrice = item.xpath('.//div[@class="unitPrice"]/span/text()')[0].replace('单价', '')
        print('单价：', unitPrice)
        # 总价
        totalPrice = item.xpath('.//div[@class="totalPrice"]/span/text()')[0] + '万'
        print("总价：", totalPrice)
        # 基本信息
        houseInfo = item.xpath('.//div[@class="houseInfo"]/a/text()')[0] + \
                    item.xpath('.//div[@class="houseInfo"]/text()')[0]
        print('基本信息：', houseInfo)

        # 房源特色信息
        r2 = requests.get(title_url, headers=headers)
        html = r2.text
        # print(html)
        html = etree.HTML(html)

        div = html.xpath('.//div[@class="introContent showbasemore"]')
        for i in div:
            # 售房详情
            houseDetail = html.xpath('.//div[@class="baseattribute clear"][1]/div[@class="content"]/text()')
            if len(houseDetail) > 0:
                houseDetail = houseDetail[0].replace('\n', '').strip()
            else:
                houseDetail = '暂无介绍'
            print('售房详情：', houseDetail)
            # 小区介绍
            communityIntroduct = html.xpath('.//div[@class="baseattribute clear"][2]/div[@class="content"]/text()')
            if len(communityIntroduct) > 0:
                communityIntroduct = communityIntroduct[0].replace('\n', '').strip()
            else:
                communityIntroduct = '暂无介绍'
            print('小区介绍：', communityIntroduct)
            # 户型介绍
            houseType = html.xpath('.//div[@class="baseattribute clear"][last()-1]/div[@class="content"]/text()')
            if len(houseType) > 0:
                houseType = houseType[0].replace('\n', '').strip()
            else:
                houseType = '暂无介绍'
            print('户型介绍：', houseType)
        print('=' * 120)

        """
            3.存储数据
        """

        # 将数据存储到数据库
        # 最后两个参数指定数据库编码必须要有，否则会报错
        conn = pymysql.connect(
            host="192.168.11.172",
            port=3306,
            user="root",
            password="root",
            database="lianjia",
            use_unicode=True,
            charset="utf8",
        )
        # 获取游标
        cursor = conn.cursor()
        # print(cursor)
        # 插入数据
        cursor.execute(
            "insert into house(title,title_url,unitPrice,totalPrice,houseInfo,houseDetail,communityIntroduct,houseType) values(%s,%s,%s,%s,%s,%s,%s,%s)",
            args=(title, title_url, unitPrice, totalPrice, houseInfo, houseDetail, communityIntroduct, houseType))
        # 提交数据
        conn.commit()
        # 回滚事务
        conn.rollback()
        # 关闭游标
        cursor.close()
    time.sleep(random.random())
