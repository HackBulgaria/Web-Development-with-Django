from celery import Celery, group

app = Celery(__name__)

app.config_from_object('settings')
