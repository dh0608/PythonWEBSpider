# """
#     案例：小说九星杀神爬虫(bs4):
# https://www.quanben.net/4/4408/
# 爬取小说章节标题，链接，章节内容
# 保存到mysql数据库
# """
from bs4 import BeautifulSoup
import requests
import random
import time

url = 'https://www.quanben.net/4/4408/'
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
r = requests.get(url, headers=headers)
r.encoding = 'gb2312'
html = r.text
# print(html)
soup = BeautifulSoup(html, 'lxml')

# 小说名
name = soup.h1.string
print(name)
# 提取章节的标签，并剔除无关章节
ls = soup.select('.chapterlist > dd > a')[10:-39]
# print(ls)
for item in ls:
    # print(type(item))

    # 文章标题
    title = item.string
    print(item.string)

    # 标题链接
    title_url = item['href']
    newurl = 'https://www.quanben.net' + title_url
    print(newurl)

    # 章节内容
    print(f'开始读取:{title}', '=' * 40)
    response = requests.get(newurl, headers=headers)
    html = response.content.decode(response.apparent_encoding, errors="ignore")
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    # 以换行分割小说文本，并且去除<br/>标签，默认为去除空白
    content = soup.select('#BookText')[0].get_text('\n', '<br/>')
    print(content)
    print(f' {title} 读取结束', '=' * 40)


    # 保存小说
    with open(f'{name}.txt', 'a', encoding='utf-8') as f:
        f.writelines([title, content])

time.sleep(random.random())
#
# import requests
# from bs4 import BeautifulSoup
# import csv
# import codecs
# import time
# import random
#
# headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2'}
# response = requests.get('https://www.quanben.net/4/4408/', headers=headers)
# html = response.content
# # encoding = response.apparent_encoding
# # print(response.decode(encoding,errors="ignore"))
#
#
# soup = BeautifulSoup(html, 'lxml')
#
# ls = soup.select('.chapterlist > dd > a')
# len = len(ls)
# for i in range(10, len):
#     title = ls[i].get_text()
#     print(ls[i].get_text())
#
#     url = "https://www.quanben.net" + ls[i].get("href")
#     r_response = requests.get(url, headers=headers)
#     r_html = r_response.content
#     r_soup = BeautifulSoup(r_html, "lxml")
#
#     content = r_soup.select("#BookText")[0]
#     print(content.get_text("\n", "<br/>"))
#
#     text = content.get_text("\n", "<br/>")
#     with codecs.open("xiaoShuo.txt", 'a', encoding="utf-8") as file:
#         wr = csv.writer(file)
#         wr.writerow([title, text])
#
# time.sleep(random.random())
