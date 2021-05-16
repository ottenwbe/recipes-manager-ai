#!/bin/bash

MAINTAINER="Beate Ottenwaelder <ottenwbe.public@gmail.com>"
DATE=$(date +"%F %T")
IS_PROD=$3
BUILDX_PARAM=$4

if [ "prod" == "${IS_PROD}" ]; then
    APP_VERSION=$(git describe --tags --always --match=v* 2> /dev/null || echo v0.0.0)
else
    APP_VERSION="development"
fi

echo "Application in Version = ${APP_VERSION}"

echo $2 | docker login -u $1 --password-stdin
docker buildx build ${BUILDX_PARAM} --platform linux/arm/v7,linux/arm64/v8,linux/amd64 --label "version=${APP_VERSION}" --label "build_date=${DATE}"  --label "maintaner=${MAINTAINER}" -t "ottenwbe/recipes-manager-recommender:${APP_VERSION}" -f Dockerfile .
