Unvanquished support for Netradiant
===================================

Installation
------------

[NetRadiant](https://netradiant.gitlab.io/) automatically fetches gamepacks it supports, you have no need to clone this repository.

In NetRadiant preferences under *Settings/Paths*, point *Engine Path* to the folder that contains the game assets. After a map compilation, the gamepack will make the editor attempt to run `/usr/bin/unvanquished` instead of a binary inside this path.

> **Note:** _The `NetRadiant-custom` fork by Garux does not work with Unvanquished because it lacks most of the required features implemented upstream since 2014. The gamepack provided with NetRadiant-custom is obsolete and will not work but using this gamepack instead will not work either because of features being missing to begin with._

Using
-----

Unvanquished has advanced file layout for maps and resources. Every map resides in separate .dpk.
Filename must obey the rule: `map-<mapname>_<mapversion>.dpk`, eg. `map-station_4.dpk`.

Unpacked files you are working with must be put into `map-<mapname>_<mapversion>.dpkdir` directory,
otherwise game will not find them.

Those are usually stored in a `pkg` directory, or a `src` directory when working with asset sources.
