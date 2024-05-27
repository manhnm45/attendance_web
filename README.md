# RUN PROJECT

### Run project(without docker):

- install project

- pip install -r requirement.txt

- turn on db(config parameter db on setting)

- cd manage_staff

- python manage.py makemigrations

- python manage.py migrate

- python manage.py createsuperuser(create user)
- python manage.py runserver

### Run project with docker
- turn on docker

- cd manage_staff

- docker compose up -d --build

- docker compose run web python manage.py makemigrations
  
- docker compose run web python manage.py migrate
  
- docker compose run web python manage.py createsuperuser

- docker compose run web python manage.py runserver
