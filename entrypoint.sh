#!/bin/sh

#python manage.py flush --no-input
python3 manage.py makemigrations
python manage.py migrate
#python manage.py initadmin
python manage.py collectstatic --no-input --clear

gunicorn core.wsgi:application --bind 0.0.0.0:8000 -w4
