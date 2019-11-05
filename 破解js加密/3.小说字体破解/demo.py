from selenium import webdriver
import re
from lxml import html

etree = html.etree

url = 'https://g.hongshu.com/content/93416/13901181.html'
browser = webdriver.Chrome()  # 设置谷歌浏览器
browser.get(url)  # 打开链接
words = browser.execute_script('return words;')  # 执行script语句，查看words数组里边的值
print(words)
html = browser.page_source  # 查看网页源码
pattern1 = re.compile(r'(<span class="context_kw\d+">.*?</span>)')  # 从网页源码中提取span标签里的内容
pattern2 = re.compile(r'class="context_kw(\d+)"')  # 提取每个span标签类名里边的数字即下标i


# m 的结果：<re.Match object; span=(5400, 5434), match='<span class="context_kw12"></span>'>
#
def func(m):
    s = m.group()   # 每个span标签
    index = int(pattern2.search(s).group(1))    # 下标
    return words[index]   # span标签里边的内容


html = pattern1.sub(func, html)  # 将 pattern1 匹配到的 span 标签按顺序在整个 html 中进行替换
html = etree.HTML(html)  # 将html字符串解析为html文档
item = html.xpath('//div[@class="rdtext"]/p/text()')  # 提取每个p标签里的文本
content = '\n'.join(item)  # 每个p标签以换行连接
print(content)

browser.close()  # 关闭浏览器
