import requests

url = 'http://politics.people.com.cn/GB/1024/index1.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
r = requests.get(url, headers=headers)
r.encoding = 'gb2312'
html = r.text
print(html)