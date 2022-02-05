#!/bin/bash

parent="/var/opt/app/fosdem_submission/html/stands-website"

cd "$parent"

git pull --no-edit origin master

#git submodule init
#git submodule update

#git pull --recurse-submodules

#git submodule sync
#git submodule update
git submodule sync
git submodule update
hugo

exit 0
