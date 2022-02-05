#!/bin/bash

parent="/var/opt/app/fosdem_submission/html/stands-website"

cd "$parent"

git pull --no-edit origin master

git submodule update --init --force --remote

hugo

exit 0
