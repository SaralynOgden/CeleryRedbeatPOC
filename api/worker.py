from celery import Celery

import celeryconfig

celery_app = Celery('tasks')
celery_app.config_from_object(celeryconfig)
