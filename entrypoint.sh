#!/bin/sh

#python manage.py flush --no-input
celery -A core worker -l info &
rm /opt/celeryd.pid
celery -A core beat -l info --pidfile=/opt/celeryd.pid -S django &
python manage.py makemigrations
python manage.py migrate
#python manage.py initadmin
python manage.py collectstatic --no-input --clear

gunicorn core.wsgi:application --bind 0.0.0.0:8000 -w4
