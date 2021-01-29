#!/bin/bash

cd /var/opt/app/fosdem_submission/html/stands-website

git pull origin master

git submodule init
git submodule update

hugo

exit 0