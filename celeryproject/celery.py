import os

from celery import Celery
from time import sleep
from timezone import timedelta
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryproject.settings')

app = Celery('celeryproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task
def add(x, y):
    sleep(10)
    return x + y

# Method-2 of using beat schedule
""" app.conf.beat_schedule = {
    'clear-session-cache': {
        'task': 'myapp.tasks.clear_session_cache',
        'schedule': 10,
    },
} """

""" app.conf.beat_schedule = {
    'clear-session-cache': {
        'task': 'myapp.tasks.clear_session_cache',
        'schedule': timedelta(seconds=10), # We can use timedelta
    },
}
 """
 
app.conf.beat_schedule = {
    'clear-session-cache': {
        'task': 'myapp.tasks.clear_session_cache',
        'schedule': crontab(minute='*/1'), # We can use crontab for each 1 minute, it can make very advanced level scheduling
    },
}

# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')