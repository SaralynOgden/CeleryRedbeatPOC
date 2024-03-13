broker_url = "redis://redis:6379/0"
result_backend = "redis://redis:6379/1"
broker_connection_retry_on_startup = False
task_routes = {'feed.tasks.import_feed': {'queue': 'orders'}}