#!/bin/bash

# usage:
#
# ./mapselect.sh mapname
#
# selects
# map-<mapname>_<ver>.pk3dir
# <ver> is a number

set +e

cd "$( dirname "${BASH_SOURCE[0]}" )"

MAP="$1"

for D in `echo map-${MAP}_*.pk3dir` ; do
    if [ -d $D ]; then
        IX=$(echo "$D" | grep -oE '_([0-9]+)\.' | tr -d '_.')
        VERSIONS[$IX]=$D
    fi
done

if (( ${#VERSIONS[@]} == 0 )); then
    LASTVER="map-${MAP}_1.pk3dir"
    mkdir "$LASTVER"
else
    LASTVER=${VERSIONS[-1]}
    if (( ${#VERSIONS[@]} > 1 )); then
        echo "You have many versions of this map, taking last ($LASTVER)"
    fi
fi

DIRS="maps music textures"

if [ ! -d "$LASTVER/maps" ]; then
    mkdir "$LASTVER/maps"
fi

for D in $DIRS ; do
    if [ -L $D ]; then
        rm $D
    fi

    if [ -e $D ]; then
        echo "$D is not a symlink! Can't delete it, aborting"
        exit
    fi

    if [ -d "$LASTVER/$D" ]; then
        ln -s "$LASTVER/$D" $D
    fi
done

echo "$LASTVER selected."
