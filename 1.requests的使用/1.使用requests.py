import requests

# 以 get 方式请求网页                     设置超时，使其停止等待响应
r = requests.get('https://www.baidu.com', timeout=0.01)
print(r)
print(type(r))  # Response 的类型
print(r.status_code)  # 状态码
print(type(r.text))  # 响应体的类型

"""
    响应的内容
"""
# print(r.text)   # 返回的是 Unicode 格式的数据
print(r.content)    # 返回的字节流数据

"""
   编码问题 
"""
print(r.encoding)   # 查看响应头部字符编码，iso-8859-1 是 Latin-1 或 "西欧语言"
print(r.apparent_encoding)  # 调用 chardet.detect()来识别文本编码
print(r.cookies)  # Cooikes

