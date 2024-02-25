from celery import Celery, shared_task
import celeryconfig

celery_app = Celery('tasks')
celery_app.config_from_object(celeryconfig)

@celery_app.task(name='tasks.add')
def add(x: int, y: int, schedule_name: str) -> int:
    print(x + y)
    return x + y
