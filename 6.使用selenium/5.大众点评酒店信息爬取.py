from selenium import webdriver
import time
import random


"""
    案例：大众点评酒店信息爬取
    url:http://www.dianping.com/shanghai/hotel/g3020p1
    爬取酒店名称，位置，价格
"""
url = 'http://www.dianping.com/shanghai/hotel/g3020p1'
browser = webdriver.Chrome()
browser.get(url)

# 找到每个酒店信息的 li 标签
ls = browser.find_elements_by_xpath('//li[@class="hotel-block"]')
print(f'共有{len(ls)}个酒店')
for item in ls:
    # 酒店名称
    hotelname = item.find_element_by_xpath('.//a[@class="hotel-name-link"]').text
    print(f'酒店名称:{hotelname}')
    time.sleep(1)
    # 位置
    hotel_place1 = item.find_element_by_xpath('.//p[@class="place"]/a').text.strip()
    hotel_place2 = item.find_element_by_xpath('.//span[@class="walk-dist"]').text.strip()
    hotel_place = hotel_place1 + hotel_place2
    print(f'酒店位置:{hotel_place}')
    time.sleep(1)
    # 价格
    price = item.find_element_by_xpath('.//div[@class="price"]//strong').text + '元'
    print(f'价格:{price}')
    print('='*130)
    time.sleep(1)
# 关闭页面
browser.close()