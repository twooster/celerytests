from celerytests.celeryapp import app
from celery.exceptions import SoftTimeLimitExceeded
import sys
import time
import os

class Suberror(Exception): pass

def do(task, sleep=None, ret=None):
    if os.environ.get("NOOP"):
        return
    try:
        print(f"Start sleep={sleep} ret={ret} pid={os.getpid()}")
        if sleep:
            time.sleep(sleep)
        if ret == "exception":
            print("Raise exception")
            raise Exception("oh no")
        if ret == "suberror":
            print("Raise suberror")
            raise Suberror("oh no")
        if ret == "retry":
            task.retry()
        if ret == "die":
            print("Killing process")
            os._exit(1)
        return ret
    except SoftTimeLimitExceeded:
        print("soft time limit exceeded, re-raising")
        raise

rowl=bool(os.environ.get("ROWL", False))

defaults = dict(
    bind=True,
    reject_on_worker_lost=rowl,
    soft_time_limit=10,
    time_limit=20,
    default_retry_delay=1
)

app.task(name="tasks.a", **defaults)(do)
app.task(name="tasks.b", **defaults, acks_late=True)(do)
app.task(name="tasks.c", **defaults, acks_late=True, max_retries=3)(do)
app.task(name="tasks.d", **defaults, acks_late=True, max_retries=3, autoretry_for=(Exception,))(do)
app.task(name="tasks.e", **defaults, acks_late=True, max_retries=3, autoretry_for=(Suberror,))(do)
