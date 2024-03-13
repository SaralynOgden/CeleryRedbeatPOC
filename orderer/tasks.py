from celery import Celery
from order import Order
from signal_type import SignalType
import celeryconfig

celery_app = Celery('tasks')
celery_app.config_from_object(celeryconfig)
signal_types = [SignalType.SKIP, SignalType.BUY, SignalType.SELL]

@celery_app.task(name="tasks.process_order")
def process_order(order: Order) -> str:
    print("Processing order: %s", order)