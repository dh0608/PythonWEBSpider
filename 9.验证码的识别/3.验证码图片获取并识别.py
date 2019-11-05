from selenium import webdriver
import time
from PIL import Image
import pytesseract

"""
    获取知网注册的验证码
"""

browser = webdriver.Chrome()
url = 'http://my.cnki.net/elibregister/commonRegister.aspx'
browser.get(url)

# 获取注册页面的截图
capture = browser.save_screenshot('./images/zhiwang.png')

img = browser.find_element_by_xpath('//div[@class="dynamic-pic"]/a/img')

# 左
left = img.location['x']
# 右
right = left + img.size['width']
# 上
top = img.location['y']
# 下
bottom = top + img.size['height']
# 打开截图
sc = Image.open('./images/zhiwang.png')
# 找到验证码并进行截图
img = sc.crop((left * 1.25, top * 1.25, right * 1.25, bottom * 1.25))
img.save('./images/code.png')
image = Image.open('./images/code.png')
# 图片转化为灰度图
image = image.convert('L')
# 二值化,指定而二值化的阈值，默认阈值127
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
        # 传入1即可将图片进行二值化处理
image = image.point(table, '1')
result = pytesseract.image_to_string(image)
print(result)
browser.quit()
