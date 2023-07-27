import os
from celery import Celery

# Configure Celery
celery = Celery(__name__)
celery.conf.broker_url = os.environ.get(
    "CELERY_BROKER_URL", "redis://redis:6379")
celery.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND", "redis://redis:6379")


@celery.task(name="create_task", bind=True)
def create_task(args):
    print('-----------------------------Creating task -----------------------------')
    return True
