from selenium import webdriver
import time
import pickle
import random

loginname = '账号用户名'
password = '账号密码'


# 模拟登陆微博
def login():
    browser = webdriver.Chrome()
    try:
        # 屏幕的高度
        browser.maximize_window()
        url = 'http://www.weibo.com/login.php'
        browser.get(url)
        time.sleep(2)

        print('正在输入用户名...')
        # 获取用户名的输入框
        name = browser.find_element_by_id("loginname")
        # 清空输入框
        name.clear()
        # 输入用户名
        name.send_keys(loginname)
        time.sleep(2)

        print('正在输入密码...')
        # 获取密码的输入框
        pwd = browser.find_element_by_name("password")
        # 清空密码输入框
        pwd.clear()
        # 输入密码
        pwd.send_keys(password)
        time.sleep(3)

        print('正在登陆...')
        # 点击登陆
        btn = browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
        btn.click()
        time.sleep(10)
        print(browser.current_url)
        # browser.quit()
        return browser
        # 获取cookie
        # cookie = browser.get_cookies()
        # print('cookies:', pickle.dumps(cookie))
        # time.sleep(5)
        # return browser
    except Exception as e:
        print(e)


# 登陆成功后爬取指定微博信息
def craw_weibo(browser, url):
    try:
        print('进入首页...')
        browser.maximize_window()
        browser.get(url)
        # 返回当前页面的高度
        height = browser.execute_script('return document.body.scrollHeight;')
        # 模拟页面向下滚动
        while True:
            print('加载页面...')
            # 向下拖动一次
            browser.execute_script('window.scrollTo(0,document.scrollHeight);')
            # 等待随机时间
            time.sleep(random.random() * 10)
            # 计算剩下的高度，和原来的比较
            new_height = browser.execute_script('return document.body.scrollHeight;')
            #
            if height == new_height:
                break
            else:
                height = new_height

        print('加载结束..')
        print('开始提取数据...')

        # 找到每个动态的标签
        ls = browser.find_elements_by_xpath('//div[@class="WB_detail"]')
        print(f'共有{len(ls)}条动态')
        for item in ls:
            # 发布人
            name = item.find_element_by_xpath('//a[@class="W_f14 W_fb S_txt1"]').text
            print(f'发布人:{name}')
            # 发布时间
            datetime = item.find_element_by_xpath('//div[@class="WB_from S_txt2"]/a')
            datetime = datetime.get_attribute('title')
            print(f'发布时间:{datetime}')
            # 发布内容
            content = item.find_elements_by_xpath('//div[@class="WB_text W_f14"]')
            if len(content) > 0:
                content = content[0].text.strip()
            else:
                print('无内容')
            print(f'发布内容{content}')
            print('=' * 130)


    except Exception as e:
        print(e)


if __name__ == '__main__':
    browser = login()
    # 指定微博首页
    url = 'https://weibo.com/u/6400679210?from=myfollow_all&is_all=1'
    craw_weibo(browser, url)
