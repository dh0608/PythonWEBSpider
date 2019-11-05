# cele.py
from celery import Celery
from celery.schedules import crontab

uri = 'redis://@127.0.0.1:6379/2'
app = Celery('tasks', broker=uri)
# 每分钟执行一次
c1 = crontab()
# 每天凌晨十二点执行
c2 = crontab(minute=0, hour=0)
# 每十五分钟执行一次
c3 = crontab(minute='*/15')
# 每周日的每一分钟执行一次
c4 = crontab(minute='*', hour='*', day_of_week='sun')
# 每周三，五的三点，七点和二十二点没十分钟执行一次
c5 = crontab(minute='*/10', hour='3,17,22', day_of_week='thu,fri')


@app.task
def send(message):
    return message


app.conf.beat_schedule = {
    'send-every-10-seconds': {
        'task': 'tasks.send',
        # 'schedule': 2.0,
        'schedule': c1,
        'args': ('Hello World',)
    },
}
