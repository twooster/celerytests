#!/bin/sh
if [ -z "$CELERY_BROKER_URL" ] ; then
  echo "CELERY_BROKER_URL must be defined, e.g.:"
  echo ""
  echo "export CELERY_BROKER_URL='amqp://user:password@localhost:5672//'"
  exit 1
fi

export NOOP=1
echo Please kill this after it clears the queues
exec ./venv/bin/celery -A celerytests.celeryapp worker -c 1 --queues tests -l info
