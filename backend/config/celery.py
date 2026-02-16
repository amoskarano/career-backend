
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("career")
app.conf.broker_url = os.getenv("REDIS_URL")
app.autodiscover_tasks()
