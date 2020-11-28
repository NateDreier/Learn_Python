#!/usr/bin/env bash
set -o errexit
set -o pipefail
set -o nounset
#for the sake of learning, learn how to automatically incrament version numbers. for now it is manual.
# automatically incriment based on whether it is going to be a major, minor or patch
black api.py

if [[ $(docker ps -a --format "{{.Names}}") == "api" ]]; then
    docker stop api
    docker rm api --force
fi

for i in $(docker images --format "{{.Repository}}:{{.Tag}}"); do
    if [[ `echo $i | cut -d':' -f1`  == "test_api" ]]; then
        current_version=$(echo $i | cut -d':' -f2)
        docker rmi $i
    fi
done

version=$1
docker build -t test_api:$version .
docker run -d -p 5000:5000 --name api test_api:$version

sleep 2

curl --location --request GET 'http://127.0.0.1:5000/store' > /dev/null 2>&1
