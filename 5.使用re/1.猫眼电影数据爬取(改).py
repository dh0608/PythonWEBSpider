import requests
from fake_useragent import UserAgent
import re, time, os
from random import randint


# 获取主页面 然后进行分析
def get_html(url):
    headers = {
        'User-Agent': UserAgent().chrome
    }
    proxies = {
        "http": "http://10.10.1.10:3128",
    }
    time.sleep(randint(5, 10))
    response = requests.get(url, headers=headers, proxies=proxies, timeout=30)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        html_text = response.text
        # print(html_text)

        return html_text
    else:
        time.sleep(randint(3, 8))
        print('----------------当前网页获取失败---------------')


# 获取每个电影的url
def get_urls(html_text):
    ids = re.findall(r'a href="/films/(\d+)" target="_blank" data-act="movies-click', html_text)
    # 获取当前页面电影的所有id
    # print(ids)
    urls = []
    for i in ids:
        url = 'https://maoyan.com/films/{}'.format(i)
        urls.append(url)
    # print(urls)
    return urls


# 解析并获取需要的信息
def get_film(html_text):
    # 分析需要获取的信息
    # 影片名称
    # 类型 地区国家  影片时长  上映时间
    # 评分  评分人数  累计票房  由于是动态获取不到
    # 剧情简介
    # 演职人员 导演  演员：饰演角色
    # 图集  暂时不处理
    # 热门短评 用户名：评语
    # 影片名称
    Ch_title = re.findall(r'<h3 class="name">(.*)</h3>', html_text)[0]
    Eng_title = re.findall(r'<div class="ename ellipsis">(.*)</div>', html_text)[0]
    print(Ch_title)

    # 类型
    type = re.findall(r'<li class="ellipsis">(.*)</li>', html_text)[0]
    # 地区
    relist = re.findall(r'<li class="ellipsis">\s+(.*)\s+/ (\d+.*)\s+</li>', html_text)[0]
    # print(relist)
    area = relist[0]
    # 时长
    duration = relist[1]
    # 上映时间
    on_time = re.findall(r'</li>\s+<li class="ellipsis">(.+)</li>\s+</ul>', html_text)[0]

    # 简介
    intro = re.findall(r'<span class="dra">(.+)</span>', html_text)[0]

    # 演职人员
    # 导演
    relist = re.findall(r'<a href="/films/celebrity/\d+" target="_blank" class="name">\s+(\S+)\s+</a>', html_text)
    # print(relist)
    director = relist[0]
    # 演员
    # 获取的是所有的演员 和饰演角色 而且有重复的  后面想办法处理

    actor_list = re.findall(
        r'<a href="/films/celebrity/\d+" target="_blank" class="name">\s+(.*)\s+</a>\s+<br /><span class="role">(.*)</span>',
        html_text)
    # print(actor_list)
    # 删除重复出现的演员名单
    # 看规律貌似是前四个  具体后面分析再说
    # 想到set集合可以去重  添加到集合然后转list 遍历出来
    try:
        for i in range(4):
            actor_list.pop(0)
    except:
        pass
    actors = ''
    for actor in actor_list:
        actor = actor[0] + '  ' + actor[1]
        actors = actors + '     ' + actor
        # print(actors)
    print(actors)
    # 热门评语
    # 用户名
    # 获取是个列表 多个用户
    username_list = re.findall(r' <span class="name">(\S+)</span>', html_text)
    # 评论
    # 获取是个列表 多个评论  每个用户对于一个评论  索引一样
    comment_list = re.findall(r'<div class="comment-content">(.*)', html_text)
    comments = ''
    for username, comment in zip(username_list, comment_list):
        comment = username + '\n' + comment + '\n\n'
        comments += comment
        # print(comments)
    # print(comments)
    # 知道需要获取的信息 然后用正则匹配出来即可
    num = 0
    try:
        film = f'影片名称:{Ch_title}({Eng_title})\n' \
            f'类型:{type} \n地区:{area} \n时长:{duration}\n上映时间:{on_time}\n' \
            f'影片简介:{intro} \n' \
            f'导演:{director} \n' \
            f'演员:\n{actors} \n\n' \
            f'热门评论:\n{comments}'
        return film, Ch_title
    except:
        film = '匹配可能有错！'
        num += 1
        return film, num


# 保存信息
def save_film(film, name):
    path = os.path.join(f'猫眼电影信息爬取/{name}.txt')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(film)


def save_urls(url):
    path = os.path.join('猫眼电影信息爬取/urls.txt')
    with open(path, 'a', encoding='utf-8') as f:
        f.write(url + '\n')


def read_urls(url, num):
    path = os.path.join('猫眼电影信息爬取/urls.txt')
    with open(path, 'a', encoding='utf-8') as f:
        f.write(f'{num}. ')
    with open(path, 'r', encoding='utf-8') as f:
        urls = f.read()
        if url in urls:
            return False
        else:
            return True


# 主方法
def main():
    # 创建文件夹  和  文件urls.txt用于存储所有的url
    try:
        os.mkdir('猫眼电影信息爬取')
    except:
        pass

    # 获取一页的源码html
    url = 'https://maoyan.com/films'
    html_text = get_html(url)

    # 根据获取到的html分析 得到每个电影的id 然后拼接成url
    urls = get_urls(html_text)

    # 然后根据每个url获取每个电影的信息
    # 遍历urls  得到url  然后分析
    num = 0
    for url in urls:
        num += 1
        print(f'----------------------获取第{num}个电影信息--------------------')
        print(url)
        # 将url保存到文件中, 每次访问文件  查看url是否存在  不存在的时候再进行爬取

        if read_urls(url, num):
            save_urls(url)
            html_text = get_html(url)
            film, name = get_film(html_text)
            save_film(film, name)
        else:
            print('---------------当前电影信息已爬取，跳过---------------')
            continue


if __name__ == '__main__':
    main()
