"""
案例：糗事百科爬虫
需求：http://www.qiushibaike.com/8hr/page/1
获取每个帖子里的用户头像链接、用户姓名、段子标题、点赞次数和评论次数

"""
import requests
from lxml import html
etree = html.etree

url = 'http://www.qiushibaike.com/8hr/page/'
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
start_page = int(input('请输入起始的页码：'))
end_page = int(input('请输入结束的页码：'))

for page in range(start_page, end_page + 1):
    pg = 'pg' + str(page)
    params = {
        'kw': pg
    }
    r = requests.get(url, params=params, headers=headers)
    html = r.text
    # print(html)
    html = etree.HTML(html)
    ls = html.xpath('.//div[@class="recommend-article"]//li')
    print('len', len(ls))




