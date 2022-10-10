#!/usr/bin/env bash

# Installing the Python packages listed in requirements.top and updating
# their dependencies, then "freeze" those versions into requirements.txt.

set -ev

cp requirements.{top,txt}
docker-compose build car-service-base
docker-compose run --rm car-service-base sh -c 'pip freeze > requirements.txt'
docker-compose build