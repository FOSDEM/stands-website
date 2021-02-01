#!/bin/bash

cd /var/opt/app/fosdem_submission/html/stands-website

git pull origin master

git submodule init
git submodule update

git pull --recurse-submodules

hugo

exit 0
