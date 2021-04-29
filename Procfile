release: python manage.py collectstatic
release: python manage.py migrate
web: gunicorn --pythonpath djangoProject djangoProject.wsgi --log-file -