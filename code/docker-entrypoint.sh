# run celery worker 
celery -A proj worker -f /var/log/app/celery.log -c 1 -l INFO -Q app -D
# migrate objects
python3 manage.py makemigrations
python3 manage.py migrate
# run django app
python3 manage.py runserver 0.0.0.0:8000