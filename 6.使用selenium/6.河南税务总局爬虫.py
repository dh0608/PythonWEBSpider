"""
案例：河南税务总局爬虫
http://henan.chinatax.gov.cn/003/index.html?NVG=0&LM_ID=1
爬取税务新闻，基层动态，媒体视点中标题，url，发布时间

"""
from selenium import webdriver
import random
import time

url = 'http://henan.chinatax.gov.cn/003/index.html?NVG=0&LM_ID=1'
browser = webdriver.Chrome()
browser.get(url)

# 找到税务新闻、基层动态、媒体视点中标题的 li 标签
ls = browser.find_elements_by_xpath('//*[@id="m_tab1"]/div[1]/ul/li')
print(f'共有{len(ls)}个分栏')
for item in ls:
    # 分类名
    item_name = item.find_element_by_xpath('.//em[@class="abtFlag"]').text
    print(f'栏目：{item_name}')
    # 获取三个分类的 url
    item_url = item.find_element_by_xpath('./a')
    item_url = item_url.get_attribute('href')
    print(f'地址：{item_url}')

    time.sleep(2)
    print('开始进入子页面....')

    browser = webdriver.Chrome()
    browser.get(item_url)

    # 找到新闻的 li 标签
    ls = browser.find_elements_by_xpath('.//ul[@class="m_news m_news_div"]/li')
    print(f'共有{len(ls)}个新闻')
    for news in ls:
        # 新闻标题
        news_title = news.find_element_by_xpath('./a').text
        print(f'新闻标题：{news_title}')

        # 新闻url
        news_url = news.find_element_by_xpath('./a').get_attribute('href')
        print(f'地址：{news_url}')

        # 新闻发布时间
        news_time = news.find_element_by_xpath('./span[@class="date"]').text
        print(f'发布时间：{news_time}')
        time.sleep(1)
        print('=' * 150)

browser.quit()
