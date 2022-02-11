#!/bin/bash

python manage.py migrate
python manage.py migrate --database=logs
python manage.py createinitialdata

gunicorn inatel.wsgi:application \
    --bind 0.0.0.0:8000 \
    --log-file=logs/gunicorn_error.log \
    --access-logfile=logs/gunicorn_access.log
fi