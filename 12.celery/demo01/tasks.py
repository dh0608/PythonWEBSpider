from celery import Celery

uri = 'redis://@127.0.0.1:6379/2'
app = Celery('tasks', backend=uri, broker=uri)  # 配置好celery的backend和broker


@app.task  # 普通函数装饰为 celery task
def add(x, y):
    return x + y
