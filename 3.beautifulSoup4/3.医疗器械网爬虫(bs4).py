"""
案例：医疗器械网爬虫(bs4):
http://www.chinamedevice.cn/
爬取大的分类
爬取产品名称，url，封面url，产品类别，批准文号，产品规格，
产品说明，生产企业，联系人，联系电话，移动电话，手机，单位地址
数据保存到 mongodb 中
"""
import requests
from bs4 import BeautifulSoup as bs
import time
import random
import re
import pymongo


# 下载指定页面
def down(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
    r = requests.get(url, headers=headers)
    # 返回当前页面以及 url
    return (r.text, r.url)


# 获取医疗器械分类
def get_classify():
    url = 'http://www.chinamedevice.cn'
    # 加载页面和链接
    html, current_url = down(url)
    # 创建  BeautifulSoup 对象
    soup = bs(html, 'lxml')
    # 获取分类的标签
    classify_ls = soup.select('a.f12 ')
    print(f'一共有{len(classify_ls)}个分类')
    for item in classify_ls:
        # 医疗器械产品分类
        classify = item.string
        print('classify：', classify)
        # 分类连接
        classify_url = url + item.attrs['href']
        print('classify_Url：', classify_url)
        get_products(classify_url)


# 获取指定类别的医疗器械
def get_products(classifyUrl):
    # 加载页面和链接
    html, current_url = down(classifyUrl)
    # 创建 BeautifulSoup 对象
    soup = bs(html, 'lxml')
    # 找到产品列表的 li 标签
    product_ls = soup.select('div.list > ul > li')
    print(f'一共有{len(product_ls)}个产品')
    for p_item in product_ls:
        # 每个产品的链接
        purl = p_item.select_one('h3 > span > a').attrs['href']
        print(f'产品链接{purl}')
        get_product_info(purl)

    # 翻页获取每一页的产品
    new_page = soup.select('a.fno')
    if len(new_page) > 0:
        new_page = new_page[-1]
        print(new_page)
        # 获取每一页网页页码的后缀
        regex = re.compile(r'(\d\.html)')
        # 将当前页面的 url 替换成下一页网页的 url
        new_page = regex.sub(new_page, current_url)
        print('下一页：', new_page)
        # 递归读取下一页
        get_products(new_page)


# 产品详情页
def get_product_info(url):
    # 加载详情页的网页、url
    html, current_url = down(url)
    # 创建 BeautifulSoup 对象
    soup = bs(html, 'lxml')
    # 产品名
    pname = soup.select_one('#main > dl > dt > h1').get_text()
    print('产品名：', pname)
    # 产品图片路径
    p_img = soup.select_one('div.img > a > img').get('src')
    print('产品图片路径：', p_img)
    # 获取产品信息的标签
    p_items = soup.select('div.text01 > ul > li')

    # 产品分类
    p_item = p_items[1].contents[1].string.strip()
    print("产品分类：", p_item)

    # 批准文号
    approval_num = p_items[3].h3.string.strip()
    print('批准文号：', approval_num)

    # 主要规格
    p_spec = p_items[4].contents[1].string.strip()
    print('主要规格：', p_spec)

    # 产品描述
    p_desc = soup.select_one('.text03').get_text().strip()
    print('产品描述：', p_desc)

    # 生产企业
    producter = soup.select_one('li.bgwhite.pt > h3 > a').get_text().strip()
    print('生产企业：', producter)
    print('=' * 200)


if __name__ == '__main__':
    get_classify()

# time.sleep(random.random())
