#!/usr/bin/env bash
# This script is used only for testing purposes

MAINTAINER="Beate Ottenwaelder <ottenwbe.public@gmail.com>"
APP_VERSION="development"
DATE=$(date +"%F %T")

docker build --label "version=${APP_VERSION}" --label "build_date=${DATE}"  --label "maintaner=${MAINTAINER}" -t "localhost:5000/ottenwbe/recipes-manager-recommender:development" -f Dockerfile . 
docker push "localhost:5000/ottenwbe/recipes-manager-recommender:development" --tls-verify=false
