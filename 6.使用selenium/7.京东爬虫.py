from selenium import webdriver
import time
import random

"""
    案例：京东爬虫
    https://www.jd.com/
    打开京东页面，搜索栏中输入“无人机”,
    滚动条拉到底部请求三次
    爬取商品名称及价格
"""

url = 'https://www.jd.com/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

time.sleep(2)

# 找到搜索输入框
input = browser.find_element_by_id('key')
# 请输入要搜索的东西
sth = '无人机'
# 输入到输入框中
input.send_keys(sth)
# 找到搜索按钮
btn = browser.find_element_by_css_selector('.button')
# 点击搜索
btn.click()

# 模拟鼠标向下滚动
for i in range(3):
    # 滚动一次 从 0 到 屏幕的高度
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(random.random() * 2)
# 获得要查询的东西的商品列表
goods_item = browser.find_elements_by_css_selector('.gl-item')
print(f'一共有{len(goods_item)}个有关的商品')

# 获得商品详情
for item in goods_item:
    # 商品标题
    goods_title = item.find_element_by_css_selector('.p-name-type-2 > a').text.strip()
    # 商品价格
    goods_price = item.find_element_by_css_selector('.p-price').text.strip()
    print(f'{goods_title}:{goods_price}')
    print('='*120)

time.sleep(3)
browser.quit()




