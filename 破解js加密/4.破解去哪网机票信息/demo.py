# 需要特别注意的是，在程序运行时，切记不要手动更改窗口大小
# 因为这样会修改到程序获得的标签的坐标信息，导致数据混乱！

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


# 从价格混淆数据中提取 price信息
def handlePrice(priceSelector):
    # 获取整个价格数据呈现区的起始横坐标
    xStart = priceSelector.location.get("x")
    # 获取数据呈现的宽度
    finalWidth = priceSelector.size.get("width")
    # 初始化一个价格数组，以显示的宽度为长度，初始值为-1，注意这儿为什么要包含finalWidth的值
    originalArray = [-1 for i in range(0, finalWidth + 1)]
    print(f"len = {len(originalArray)}")
    firstLevelLst = priceSelector.find_elements_by_xpath(".//b")
    for firstLevel in firstLevelLst:
        secondLevelLst = firstLevel.find_elements_by_xpath("./i")
        # 如果有下一级，就处理下一级的数字
        if secondLevelLst:
            for secondLevel in secondLevelLst:
                # 获取相对坐标值，也就是在数组中的起始位置
                xStartSecond = secondLevel.location.get("x") - xStart
                # 获取这个字符所占的宽度
                xWidthSecond = secondLevel.size.get("width")
                # 将数组中这个位置的值替换成这个网页中的文本
                originalArray[xStartSecond] = secondLevel.text
                # 这个字符所占剩余部分的空间，全都置成 -1
                for i in range(xStartSecond + 1, xStartSecond + xWidthSecond - 1):
                    originalArray[i] = -1
                print(f"secondX = {xStartSecond}, secondLevel = {secondLevel.text}, xWidthSecond = {xWidthSecond}")
        else:
            # 获取相对坐标值，也就是在数组中的起始位置
            xStartFirst = firstLevel.location.get("x") - xStart
            # 获取这个字符所占的宽度
            xWidthFirst = firstLevel.size.get("width")
            # 将数组中这个位置的值替换成这个网页中的文本
            originalArray[xStartFirst] = firstLevel.text
            # 这个字符所占剩余部分的空间，全都置成 -1
            for i in range(xStartFirst + 1, xStartFirst + xWidthFirst):
                originalArray[i] = -1
            print(f"firstX = {xStartFirst}, firstLevel = {firstLevel.text}, xWidthFirst = {xWidthFirst}")
    # 从originalArray数组中，把标记过的数据取出来
    finalPrice = ""
    for elem in originalArray:
        if elem != -1:
            print(f"elem = {elem}", end=', ')
            finalPrice += str(elem.strip())
    return int(finalPrice) if finalPrice != "" else 0


if __name__ == "__main__":
    # chrome_options = webdriver.ChromeOptions()
    # 载入xpath Helper插件，方便调试
    # extension_path = 'C:\Users\年轮\Downloads\xpath_helper'
    # chrome_options.add_extension(extension_path)

    # 启动浏览器，注意这儿是已经配置过chromedriver.exe的环境变量了，才可以直接使用，不填路径
    # browser = webdriver.Chrome(chrome_options=chrome_options)
    browser = webdriver.Chrome()
    browser.maximize_window()

    qunaerUrl = "https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=拉萨&searchArrivalAirport=深圳&searchDepartureTime=2019-10-08&searchArrivalTime=2019-10-10&nextNDays=0&startSearch=true&fromCode=LXA&toCode=SZX&from=flight_dom_search&lowestPrice=null"
    browser.get(qunaerUrl)
    # 为了简化逻辑，此处使用等待10秒
    # 其实更精确的做法是，等待页面中某个标志性元素加载成功
    time.sleep(5)

    # 这个地方尤其需要注意：不要使用page_source来提取数据，因为page_source是指网页源代码
    # 和我们用其他方式requests，scrapy抓下来的页面没有任何区别
    # 千万不要误解成，page_source就是渲染后的页面数据，这是错误的
    # selenium渲染后的是一个DOM对象，目前是没有办法将这种数据弄下来。
    # 一般来说，我们既然选择了用selenium来抓取数据，大部分情况也是因为网页源代码中无法提取到有效数据
    # 而很多培训教程中，总是提到用selenium内置的数据提取器来提取数据速度非常慢，建议使用re，xpath直接从page_source中提取数据
    # 这是需要辩证的去看的。
    # pageSource = browser.page_source
    # print(f"{pageSource}")

    allAirLst = browser.find_elements_by_xpath("//div[@class='b-airfly']")
    for airInfo in allAirLst:
        name = airInfo.find_element_by_xpath(".//div[@class='air']/span").text
        startTime = airInfo.find_element_by_xpath(".//div[@class='sep-lf']/h2").text
        endTime = airInfo.find_element_by_xpath(".//div[@class='sep-rt']/h2").text
        priceSelector = airInfo.find_element_by_xpath(".//span[@class='prc_wp']")
        finalPrice = handlePrice(priceSelector)
        print(f"\n####{name}           {startTime}           {endTime}          price:{finalPrice}")
