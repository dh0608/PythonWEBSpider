import pytesseract
from selenium import webdriver
from PIL import Image


def get_capture():
    browser = webdriver.Chrome()
    url = 'https://www.baidu.com'
    # 打开指定网址
    browser.get(url)
    # 对网页进行截图
    browser.save_screenshot('./images/baidu.png')
    # 获取 百度logo 的标签
    logo = browser.find_element_by_xpath('//div[@id="lg"]/img[1]')
    # 用 location 获取图片的位置
    # 左
    left = logo.location['x']
    # 右
    right = left + logo.size['width']
    # 上
    top = logo.location['y']
    # 下
    bottom = top + logo.size['height']
    # 也可以直接手动输入位置,但这种方式要求给出准确的坐标
    rangle = (806, 382, 913, 415)

    # 打开已经保存的网页截图
    sc = Image.open('./images/baidu.png')
    # 裁剪图片获取 logo,
    # 这里把图片的位置都 *1.25是因为win10默认缩放文本1.25倍，
    # 因此需要在这里乘回来，否则截图会出错
    logo = sc.crop((left * 1.25, top * 1.25, right * 1.25, bottom * 1.25))
    # logo = sc.crop(rangle)
    logo.save('./images/logo.png')
    browser.quit()


get_capture()
