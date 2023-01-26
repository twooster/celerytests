#!/bin/sh
if [ -z "$CELERY_BROKER_URL" ] ; then
  echo "CELERY_BROKER_URL must be defined, e.g.:"
  echo ""
  echo "export CELERY_BROKER_URL='amqp://user:password@localhost:5672//'"
  exit 1
fi

exec ./venv/bin/celery -A celerytests.celeryapp worker -c 10 --queues tests -l debug
