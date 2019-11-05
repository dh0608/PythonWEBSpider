"""
    1.查询参数(params)
        params 接收一个字典或者字符串的查询参数，字典类型自动转换为 url 编码，不需要
    urlencode()
    2.添加 headers
        如果请求里边没有 headers 信息，它其中包含了 User-Agent，也就是浏览器的标识信息。
    如果不加这个，网站会检测到是爬虫，禁止抓取

"""
import requests

kw = {'wd': '长城'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)
print(response.text)
# print(response.json())
print(response.encoding)
