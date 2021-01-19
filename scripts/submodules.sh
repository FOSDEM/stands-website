#!/bin/bash

while read submodule; do
    path=$(echo "$submodule" | awk '{print $1}')
    url=$(echo "$submodule" | awk '{print $2}')
    git submodule add "$url" "$path"
done <scripts/submodules