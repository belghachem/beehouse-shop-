set -o errexit
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.PY runserver 0.0.0.0:8000
