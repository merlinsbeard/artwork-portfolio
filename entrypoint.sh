#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
echo Starting Gunicorn.
exec gunicorn clever_red.wsgi:application \
    --bind 0.0.0.0:8000 \
    --name artwork \
    --workers $GUNICORN_WORKERS \
    --log-level=info \
    --access-logfile - \
    --error-logfile - \
"$@"
echo woot
