#!/bin/bash

# Variables

APP_DIR=/vagrant/clever_red/clever_red
VENV_LOC=/home/vagrant/venv/jobvenv
PORT=8002
# Run virtualenv

cd $APP_DIR
source $VENV_LOC/bin/activate

# RUN DJANGO GUNICORN

exec gunicorn --bind 0.0.0.0:$PORT clever_red.wsgi:application --log-file=- &
