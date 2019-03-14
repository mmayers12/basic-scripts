#!/bin/bash

for i in $(ls); do
    if [ $i != "README.md" ] && [ $i != 'link_to_bin.sh' ]; then
        ln -s `pwd`'/'$i ~/bin/$i
    fi
done

