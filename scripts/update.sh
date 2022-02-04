#!/bin/bash

parent="/var/opt/app/fosdem_submission/html/stands-website"

cd "$parent"

git pull --no-edit origin master

#git submodule init
#git submodule update

#git pull --recurse-submodules

git submodule sync
git submodule update
hugo

exit 0


for d in $(find content/stands -maxdepth 1 -type d); do

	basename=$(basename "$d")
	if [ "$basename" != "stands" ]; then
                cd "$d"
                remote=$(git remote -v | head -n 1 | awk '{ print $2 }')
                if [ "$remote" != "https://github.com/FOSDEM/stands-website.git" ]; then
                        
                        git stash
                        echo "$d"
                        git branch > /dev/null
                        if [ "$?" == "0" ]; then
                                git pull origin $(git branch | tail -1 | sed 's/*//' | awk '{print $1}')
                        fi
                fi
                cd "$parent"
	fi

done


for d in $(find static/stands -maxdepth 1 -type d); do

        basename=$(basename "$d")
        if [ "$basename" != "stands" ]; then
                cd "$d"
                if [ "$remote" != "https://github.com/FOSDEM/stands-website.git" ]; then
                        git stash
                        echo "$d"
                        git branch > /dev/null
                        if [ "$?" == "0" ]; then
                                git pull origin $(git branch | tail -1 | sed 's/*//' | awk '{print $1}')
                        fi
                fi
                cd "$parent"
        fi

done


