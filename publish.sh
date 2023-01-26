#!/usr/bin/env bash
if [ -z "$CELERY_BROKER_URL" ] ; then
  echo "CELERY_BROKER_URL must be defined, e.g.:"
  echo ""
  echo "export CELERY_BROKER_URL='amqp://user:password@localhost:5672//'"
  exit 1
fi


task="${1:?Task required}"
sleep=${2:-1}
ret=${3:-}

case "$ret" in
  "" | "die" | "suberror" | "exception" | "retry")
    # noop
  ;;
  *)
    echo "Return value, if provided, must be one of: die, suberror, exception, retry"
    exit 1
  ;;
esac

exec ./venv/bin/celery  -A celerytests.celeryapp call --queue tests tasks."$task" -k '{"sleep":'"$sleep"', "ret":"'"$ret"'"}'
