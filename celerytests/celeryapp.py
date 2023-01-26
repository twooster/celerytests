import celerytests.celeryconfig
from celery import Celery

app = Celery('celerytests')
app.config_from_object(celerytests.celeryconfig)
