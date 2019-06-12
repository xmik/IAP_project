#!/bin/bash

# TODO: wait for postgres to be ready?

cd /usr/src/app
python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000

# curl localhost:8000/branch_offices
# curl -i -L 127.0.0.1:8000/branch_offices
