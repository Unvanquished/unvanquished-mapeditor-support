Unvanquished support for DarkRadiant
====================================

Installation
------------

DarkRadiant is not yet usable for Unvanquished, but if you're a developer you can be interested in the game file for testing purpose.

Download the [game file](games/unvanquished.game) and put it in `install/games/` directory within darkadiant one.

Set the engine path in DarkRadiant preferences.

Using
-----

Keep in mind game directory must contains a `pkg` directory.

Unvanquished has advanced file layout for maps and resources. Every map resides in separate .dpk.
Filename must obey the rule: `map-<mapname>_<mapversion>.dpk`, eg. `map-station_4.dpk`.

Unpacked files you are working with must be put into `map-<mapname>_<mapversion>.dpkdir` directory,
otherwise game will not find them.
