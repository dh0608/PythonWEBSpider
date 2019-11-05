"""
    要想检查某个主机的 SSL 证书，你可以使用 verify 参数（也可以不写）
如果 SSL 证书验证丌通过，戒者丌信任服务器的安全证书，则会报出 SSLError，比如 12306：

"""
import requests
r = requests.get('https://www.12306.cn/mormhweb/', verify=True)
print(r.text)