#!/bin/bash
cd /Dog-Breed-Classification-DRF-API
echo "yes" | python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
exec gunicorn --workers 3 --bind unix:/apisocket/apisocket.sock deeplearningapp.wsgi:application