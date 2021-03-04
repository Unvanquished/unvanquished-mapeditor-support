Unvanquished support for DarkRadiant
====================================

Installation
------------

DarkRadiant is not yet usable for Unvanquished, but if you're a developer you can be interested in the game file for testing purpose.

Download the [game file](games/unvanquished.game) and put it in `install/games/` directory before compilation when installing from sources, or in `/usr/share/netradiant/games` directory otherwise (or the related path specific to your operating system hierarchy).

Set the [UnvanquishedAssets](https://github.com/UnvanquishedAssets/UnvanquishedAssets) repository as engine path in DarkRadiant preferences, set `pkg` as `fs_game` and `src` as `fs_game_base`.

Download the [def file](pkg/def/entities.def) and store it as `pkg/def/entities.def` in the `UnvanquishedAssets` repository.

> **Note:** _DarkRadiant reads the Q3 legacy brush format used by Unvanquished, but only write the Q3 non-legacy brush one, so the map is expected to be converted on writing._

Using
-----

Unvanquished has advanced file layout for maps and resources. Every map resides in separate .dpk.
Filename must obey the rule: `map-<mapname>_<mapversion>.dpk`, eg. `map-station_4.dpk`.

Unpacked files you are working with must be put into `map-<mapname>_<mapversion>.dpkdir` directory,
otherwise game will not find them.

Those are usually stored in a `pkg` directory, or a `src` directory when working with asset sources.