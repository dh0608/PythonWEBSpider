import redis
import json

r = redis.Redis(host='127.0.0.1', port=6379, db=3)

keys = r.keys()
#print('\u79c0\u5c7f')
for key in keys:
    res = r.get(key)
    res = json.loads(res.decode('utf-8'))
    print(res.get('result'))
    all = str(res.get('result'))
    filename = 'weather.txt'
    with open(filename, 'a', encoding='utf-8')as f:
        f.write(all+'\n')


