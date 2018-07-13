from __future__ import absolute_import

import os

from datetime import timedelta
from celery import Celery
from celery.schedules import crontab

from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'url_shortner.settings')

app = Celery('url_shortner')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('url_shortner.settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    CELERY_ACCEPT_CONTENT = ['json'],
    CELERY_TASK_SERIALIZER = 'json',
    CELERY_RESULT_SERIALIZER = 'json',
    BROKER_URL = 'amqp://shurl:shurlwordpass@localhost:5672/shurlhost',
    CELERYD_LOG_FILE=os.getcwd()+"/logs/celery.log",
    # BROKER_URL = 'django://',
    CELERY_RESULT_BACKEND = "amqp",
    CELERY_IMPORTS = ("shortner_app.tasks"),
    CELERY_ALWAYS_EAGER = False,
    # CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
    # CELERY_TIMEZONE = 'Europe/London'
    CELERY_TIMEZONE = 'UTC',
    CELERY_IGNORE_RESULT=True,
    CELERYBEAT_SCHEDULE = {
        # 'debug-test': {
        #     'task': 'trip.tasks.test_celery',
        #     'schedule': timedelta(seconds=5),
            # 'args': (1, 2)
        # },
    }
)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
