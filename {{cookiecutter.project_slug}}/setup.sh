#!/bin/bash

# create virtual environment
cd main

python3 -m venv venv
source venv/bin/activate

# install packages from requirements.txt

pip install -r requirements.txt


# run Django migrations
python manage.py makemigrations
python manage.py migrate
python manage.py runserver