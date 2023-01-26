import os

broker_url = os.environ['CELERY_BROKER_URL']

broker_use_ssl = os.environ.get('CELERY_USE_SSL', False)
broker_heartbeat = None

worker_concurrency = int(os.environ.get('CELERY_WORKER_CONCURRENCY', 10))

worker_prefetch_multiplier = int(os.environ.get('CELERY_PREFETCH_MULTIPLIER', 2))

# Send events so the worker can be monitored by tools like celerymon
worker_send_task_events = True

accept_content = ["json"]
task_serializer = "json"
result_serializer = "json"

task_ignore_result = True

imports = ('celerytests.tasks',)
