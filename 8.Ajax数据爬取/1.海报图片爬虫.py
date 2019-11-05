"""
    海报图片爬虫
    http://www.haibao.com/
    http://pic.haibao.com/hotimage/
    爬取海报图片
"""

import requests
from lxml import html
import datetime
etree = html.etree

url = 'http://pic.haibao.com/hotimage/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Referer': 'http://pic.haibao.com/'
}

html = requests.get(url, headers=headers).text
# print(html)
html = etree.HTML(html)

# 封面图片
# ls = html.xpath('//div[@class="pagelibox"]//img/@data-original')
# 封面的大图
ls = html.xpath('//div[@class="imginfor-fr"]//a[2]/@originurl')
len = len(ls)
print(f'共有{len}张图片')

for item in ls:
    # 打开当前页面的每张封面图片
    images = requests.get(item, headers=headers).content
    print(f'正在下载{item}')

    # 保存的图片名
    img_name = './images/haibao/' + item.split('/')[-1]
    with open(img_name, 'wb') as f:
        f.write(images)
        print(f'正在保存{img_name}')
        print('='*150)

# 模拟Ajax，爬取更多的图片
base_url = 'http://pic.haibao.com/ajax/image:getHotImageList.json'
# 请求的图片数和刚打开时一样
# skip = len(ls)
# 初始页数
page = 1
# 爬取前10页的图片
while page <= 10:
    #        周五 九月
    # stamp: Fri Sep 13 2019 17:08:33 GMT 0800 (中国标准时间):
    # 构造一个格式化的时间字符串
    format_time = '%a %b %Y %H:%M:%S GMT 0800'
    # 获取当前时间的格式化字符串 ，这里使用的是世界时间
    stamp = datetime.datetime.utcnow().strftime(format_time)
    stamp += ' (中国标准时间)'
    print('stamp:', stamp)
    # 将时间添加到 url 中
    new_url = base_url + '?stamp=' + stamp
    # 请求的照片数量
    data = {
        'skip': len
    }
    # 发送 post 请求
    data = requests.post(new_url, headers=headers, data=data).json()
    print(f'---------------第{page}页---------------------')
    # 请求照片数
    skip = data['result']['skip']
    print(f'请求照片数：{skip}')
    # 网页源码
    html = data['result']['html']
    # 爬取数据
    html = etree.HTML(html)
    ls = html.xpath('//div[@class="imginfor-fr"]//a[2]/@originurl')
    for item in ls:
        # 打开当前页面的每张封面图片
        images = requests.get(item, headers=headers).content
        print(f'正在下载{item}')

        # 保存的图片名
        img_name = './images/haibao/' + item.split('/')[-1]
        with open(img_name, 'wb') as f:
            f.write(images)
            print(f'正在保存{img_name}')
            print('=' * 150)


