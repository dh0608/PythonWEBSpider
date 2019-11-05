# 分析

# 1.找到需求
# 爬取猫眼电影 每个电影的详情信息

# 2.怎么做
# 找到url 获取html

# 3.数据处理
# 在找到的html源码中 处理数据 得到想要的内容
# 比如片名 ，演员名  ，上映时间  ，地区 等等


# 用到的模块
import requests
from fake_useragent import UserAgent

# 文件保存和程序休眠  数据处理
import os, time, re
from random import randint
# time.sleep(randint(5,10))

# 定义方法 分工明确

# 获取网页html源码
# 传入url的到html
def grt_html(url):
    headers = {
        'User-Agent': UserAgent().chrome
    }
    proxies = {
        # 'http': 'http://221.2.175.238:8060',
        'https': 'https://218.60.8.99:3129',

    }
    # 'https://ip.cn'  验证ip的地址
    # print(headers)
    response = requests.get(url, headers=headers, proxies=proxies)
    print(response)
    if response.status_code == 200:
        html = response.text
        print(html)
        return html
    else:
        print('-----------网页访问失败，请稍后尝试---------------')


# 得到想要的信息
# 传入html  然后数据处理  得到想要的数据
def get_xinxi(html):
    # 需要获取到的信息
    # 电影名称 类型 地区/片长  上映时间 地区
    name = re.findall(r'<h3 class="name">(.+)</h3>\s+<div class="ename ellipsis">(.+)</div>', html)[0]
    name_zh = name[0]
    name_en = name[1]
    type = re.findall(r'<li class="ellipsis">(.+)</li>\s+<li class="ellipsis">', html)[0]
    lists = re.findall(r'<li class="ellipsis">\s+(.+)\s+/ (.+)\s+</li>', html)[0]
    diqu = lists[0]
    times = lists[1]
    ontime = re.findall(r'<li class="ellipsis">(.+)</li>\s+</ul>', html)[0]

    name = name_zh
    xinxi = f'电影名称：{name_zh}（{name_en}）\n' \
        f'电影类型：{type} \n' \
        f'地区：{diqu}\n' \
        f'时长：{times}\n' \
        f'上映时间：{ontime}'
    print('--------------------信息----------------')
    print(xinxi)
    return name, xinxi


# 得到信息  保存  name文件名字
def get_save(name, xinxi):
    with open(f'{name}.txt', 'w', encoding='utf-8') as f:
        f.write(xinxi)
        print(f'---------------电影《{name}》信息爬取完毕，已保存！--------------')


# 定义主方法
def main():
    print('-----------------------开始爬取数据-----------------')
    url = 'https://maoyan.com/films/342903'
    html = grt_html(url)
    name, xinxi = get_xinxi(html)
    get_save(name, xinxi)


if __name__ == '__main__':
    main()
