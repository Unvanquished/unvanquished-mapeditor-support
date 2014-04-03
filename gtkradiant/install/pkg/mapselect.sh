#!/bin/bash
#
# usage:
#
# ./mapselect.sh mapname
#
# selects
# map-<mapname>_source.pk3dir
#
# you should copy your source dir when you finish its version
# cp -R map-mymap_source.pk3dir map-mymap_1.pk3dir
#
# to clean up all symlinks:
#
# ./mapselect.sh


# when you create new dirs or files in your map dir
# and want symlinks to be created for them
# add them here:
DIRS='env maps music textures sound'
FILES='scripts/${M}.shader scripts/q3map2_${M}.shader scripts/${M}.arena'


set +e
MAP="$1"
REQUIRED_DIRS="maps scripts textures"
REQUIRED_FILES="maps/${MAP}.map scripts/${MAP}.shader scripts/q3map2_${MAP}.shader scripts/${MAP}.arena"

# cleanup symlinks

M='*'
FLIST=$(eval "echo $FILES")
echo "Removing symlinks.."
for F in $FLIST ; do
  if [ -L "$F" ]; then { rm "$F" ; echo "  $F" ; } ; fi
done
for D in $DIRS ; do
  if [ -L "$D" ]; then { rm "$D" ; echo "  $D" ; } fi
done

# exit if no map chosen

if [ -z "$MAP" ]; then exit ; fi

# autocreate dirs and files

MAPDIR="map-${MAP}_source.pk3dir"

echo "Autocreating.."
for D in $REQUIRED_DIRS ; do
  if [ ! -d "$MAPDIR/$D" ]; then { mkdir -p "$MAPDIR/$D" ; echo "  $D" ; } fi
done
for F in $REQUIRED_FILES ; do
  if [ ! -f "$MAPDIR/$F" ]; then { touch "$MAPDIR/$F" ; echo "  $F" ; } fi
done

# symlinks

M="$MAP"
FLIST=$(eval "echo $FILES")
echo "Making symlinks.."
for D in $DIRS ; do
  if [ -d "$MAPDIR/$D" ]; then { ln -s "$MAPDIR/$D" "$D" ; echo "  $D" ; } fi
done
for F in $FLIST ; do
  if [ -f "$MAPDIR/$F" ]; then { ln -s "$(pwd)/$MAPDIR/$F" "$F" ; echo "  $F" ; } fi
done

echo "Done. Selected: $MAPDIR"
