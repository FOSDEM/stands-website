#!/bin/bash

parent="/var/opt/app/fosdem_submission/html/stands-website"

cd "$parent"

git pull origin master

#git submodule init
#git submodule update

#git pull --recurse-submodules


for d in $(find content/stands -maxdepth 1 -type d); do

	basename=$(basename "$d")
	if [ "$basename" != "stands" ]; then
		cd "$d"
		git branch > /dev/null
		echo "$d"
		if [ "$?" == "0" ]; then
			git pull origin $(git branch | tail -1 | sed 's/*//' | awk '{print $1}')
		fi
		cd "$parent"
	fi

done

hugo

exit 0
