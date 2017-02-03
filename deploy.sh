#!/bin/bash

set -e

# Build container
docker-compose build
# Run container
docker-compose up -d
# Make database, etc.
docker-compose run web python manage.py migrate
# Create admin
docker-compose run web python manage.py createsuperuser

