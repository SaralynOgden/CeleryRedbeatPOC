from kombu import Queue
import random
from celery import Celery
from order import Order
from signal_type import SignalType
import celeryconfig

celery_app = Celery('tasks')
celery_app.config_from_object(celeryconfig)
signal_types = [SignalType.SKIP, SignalType.BUY, SignalType.SELL]

@celery_app.task(name='tasks.add')
def add(x: int, y: int, schedule_name: str) -> int:
    print(x + y)
    return x + y

@celery_app.task(name="tasks.check_for_trade")
def check_for_trade(symbol_name: str, schedule_name: str):
    print('Checking for trade on {}'.format(symbol_name))
    price = random.randint(1,101)
    weighted_random = 0
    if price <= 45:
        weighted_random = 1
    elif price >= 55:
        weighted_random = 2
    else:
        weighted_random = 0
    signal_type = signal_types[weighted_random]
    if signal_type != SignalType.SKIP:
        print('got a signal')
        print(signal_type)
        print(price)
        order = Order(symbol_name, signal_type, price, 0)
        print('sending order')
        task = celery_app.send_task('tasks.process_order', args=['order'], kwargs={}, queue='orders')
        
@celery_app.task(name="tasks.process_order")
def process_order(order: Order):
    return