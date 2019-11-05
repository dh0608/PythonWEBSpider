import execjs
import requests
import re

node = execjs.get()
print(node.name)  # js的执行环境
file = './demo.js'  # js解密文件路径
ctx = node.compile(open(file, 'r', encoding='utf-8').read())  # 读取并编译js文件

url = 'http://ac.scmor.com/'
headers = {
    'Referer': 'http://ac.scmor.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Sec-Fetch-Mode': 'no-cors'
}
r = requests.get(url, headers=headers)
html = r.content.decode(r.apparent_encoding)  # 网页源码
# print(html)
# 通过网页源码看到 '现在访问'并没有链接，又看到它里边有一个 js 函数（visit(url)）来调用，
# 因此可以得出链接是动态生成的, 要调用它我们只需要把里边的 url 提取(re)出来就行了。
# autourl[1] = "AD0mWAw2VVYgWiAdDB4LHQwqaxY2XxcVL0M9FiEYTxM="
pattern = re.compile(r'autourl.*?"(.*?)"')
all = pattern.findall(html)
print(f'共有{len(all)}个链接')

for index, item in enumerate(all, 1):  # enumerate函数：可以将可遍历的数据对象组合成带有索引的数据
    href = ctx.call('strdecode', item)  # 通过调用 strdecode 解密方法来对 url 解密
    print(f'第{index}个链接:{href}')
