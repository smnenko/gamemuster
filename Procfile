web: python3 manage.py migrate && wait && python3 manage.py loaddata initial.json && wait && gunicorn backend.wsgi:application --preload --log-file -
beat: celery -A backend beat -l info
worker: celery -A backend worker -l INFO