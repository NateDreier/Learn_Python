#!/usr/bin/env bash

#for the sake of learning, learn how to automatically incrament version numbers. for now it is manual.
# automatically incriment based on whether it is going to be a major, minor or patch

for i in $(docker images --format "{{.Repository}}:{{.Tag}}"); do
    if [[ `echo $i | cut -d':' -f1`  == "test_api" ]]; then
        current_version=$(echo $i | cut -d':' -f2)
        docker rmi $i
    fi
done

version=$1

docker build -t test_api:$version .
docker run -d -p 5000:5000 test_api:$version
