import requests
import random
import time
import hashlib

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

word = input('请输入要翻译的词：')
# 经过分析， 发现表单里边的数据 sign 和 salt是加密的，因此需要找到破解办法
# 在所有异步加载的js中，查找 sign 或者 salt关键字发现在 fanyi.min.js文件中
# 找到定义的加密函数：
#   var r = function(e) {
#         var t = n.md5(navigator.appVersion)
#           , r = "" + (new Date).getTime()
#           , i = r + parseInt(10 * Math.random(), 10);
#         return {
#             ts: r,
#             bv: t,
#             salt: i,
#             sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
#         }
#     };
# 分析可以得到 salt是时间戳加上一位随机生成的一位 0-10之间的数字
# sign 由四部分组成，开头和结尾都是固定的字符串，e为查询的单词，i为salt，最后拼接在一起后进行md5加密
ctime = int(time.time() * 1000)  # 这里只取前13位
salt = str(ctime + random.randint(1, 10))
client = 'fanyideskweb'
key = "n%A-rKaT5fb[Gy?;N5@Tj"
sign = hashlib.md5((client + word + salt + key).encode('utf-8')).hexdigest()
FormData = {
    'i': word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': client,
    'salt': salt,
    'sign': sign,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
    'typoResult': 'false'
}
headers = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Length': '251',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-557501186@10.169.0.83; JSESSIONID=aaajdDIX6Wzp8gA5GnL2w; OUTFOX_SEARCH_USER_ID_NCOO=1746189910.5843475; ___rl__test__cookies=' + str(
        ctime),
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
r = requests.post(url, headers=headers, data=FormData)
# print(r.json())
result = r.json()['translateResult'][0][0]['tgt']
print(f'翻译结果为:{result}')