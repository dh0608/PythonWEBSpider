from celery import Celery
from celery import Task

app = Celery('tasks', backend='redis://@127.0.0.1:6379/2', broker='redis://127.0.0.1:6379/2')
app.config_from_object('celery_config')


@app.task(bind=True)
def period_task(self):
    print('period task done: {0}'.format(self.request.id))
