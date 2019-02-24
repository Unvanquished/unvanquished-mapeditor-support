Unvanquished support for Netradiant
===================================

Installation
------------

NetRadiant automatically fetches gamepacks it supports, you have no need to clone this repo.

In the Netradiant preferences under *Settings/Paths*, point *Engine Path* to the folder that contains the game assets. After a map compilation, the gamepack will make the editor attempt to run `/usr/bin/unvanquished` instead of a binary inside this path.

Using
-----

During the first start Radiant tries to install additional files into your game directory.
Make sure it's writable for you.

Keep in mind game directory must contain `pkg` directory (like `baseq3` was in Quake 3 dir).

Unvanquished has advanced file layout for maps and resources. Every map resides in separate .dpk.
Filename must obey the rule: `map-<mapname>_<mapversion>.dpk`, eg. `map-station_4.dpk`.

Unpacked files you are working with must be put into `map-<mapname>_<mapversion>.dpkdir` directory,
otherwise game will not find them.
