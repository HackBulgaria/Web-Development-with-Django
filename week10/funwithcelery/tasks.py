from celery import group
from celery_app import app


@app.task(bind=True, max_retries=1)
def retry_task(self):
    print('IN TASK')
    exc = Exception('retrying')
    self.retry(exc=exc, countdown=60)

@app.task
def add(x, y):
    return x + y


@app.task
def just_printing(*args, **kwargs):
    print('Someone called me: just_printing')
    print(args, kwargs)


@app.task
def group_adds(ns):
    return group(add.s(*n) for n in ns)()
