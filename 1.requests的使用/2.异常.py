import requests
"""
    异常
"""
try:
    requests.get(' http://www.baidu.com/', timeout=0.01)
except Exception as e:
    print(e)