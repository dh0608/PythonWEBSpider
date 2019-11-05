from selenium import webdriver
from selenium.webdriver.common.by import By


# chrome 无界面模式
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# brower = webdriver.Chrome(chrome_options=chrome_options)
brower = webdriver.Chrome()
url = 'https://item.jd.com/5089267.html'
brower.get(url)
# 提取京东商品的价格
# 方式一
price1 = brower.find_element(By.CLASS_NAME, 'J-p-5089267')
print(price1.text)
# 方式二
price2 = brower.find_element_by_css_selector('.J-p-5089267')
print(price2.text)
# 方式三
price3 = brower.find_element_by_xpath('//span[@class="price J-p-5089267"]')
print(price3.text)

# 截屏
# brower.save_screenshot('./images/iphone8.png')
# 超长截图
# 这里需要使用无界面浏览器来实现网页的全部快照

brower.close()

