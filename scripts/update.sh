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
if [ "$?" -ne 0 ]; then
  git submodule update --init --force --remote
fi
git submodule update

if [ "$?" -ne 0 ]; then
  git submodule update --init --force --remote
fi

if [ "$?" -ne 0 ]; then
  exit $?
fi

hugo

exit 0
