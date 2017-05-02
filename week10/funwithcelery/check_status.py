import sys

from celery.result import AsyncResult

from celery_app import app

task_id = sys.argv[1]


result = AsyncResult(id=task_id, app=app)

attrs = ['ready', 'state', 'result']

for attr in attrs:
    v = getattr(result, attr)

    if callable(v):
        v = v()

    print(attr, v)
