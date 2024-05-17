Run project:
- install project
-pip install -r requirement.txt
-turn on db(config parameter db on setting)
-cd manage_staff
-python manage.py makemigrations
-python manage.py migrate
-python manage.py createsuperuser(create user)
-python manage.py runserver

Run project wit docker
-cd manage_staff
-docker compose up -d
-docker compose run web python manage.py makemigrations
-docker compose run web python manage.py createsuperuser
-docker compose run web python manage.py runserver
