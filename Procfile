web: python manage.py collectstatic --noinput
release: python manage.py migrate
web: gunicorn --pythonpath djangoProject djangoProject.wsgi --log-file -