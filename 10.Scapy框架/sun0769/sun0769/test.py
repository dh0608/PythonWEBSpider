import requests

url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
r = requests.get(url, headers=headers)
r.encoding = 'gb2312'
html = r.text
print(html)