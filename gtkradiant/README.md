Unvanquished support for GtkRadiant
===================================

Supported versions
------------------

* GtkRadiant 1.6

Installation
------------

GtkRadiant automatically fetches gamepacks it supports, you have no need to clone this repo.

List of available games is hardcoded, so you will need patched version.
Use my repo https://github.com/neumond/GtkRadiant
It doesn't differ a lot, you'll get a version as close to official as possible.
In future it can be merged to official repository.

Using
-----

During the first start Radiant tries to install additional files into your game directory.
Make sure it's writable for you.

Keep in mind game directory must contain `pkg` directory (like `baseq3` was in Quake 3 dir).

Unvanquished has advanced file layout for maps and resources. Every map resides in separate .pk3.
Filename must obey the rule: `map-<mapname>_<mapversion>.pk3`, eg. `map-station_4.pk3`.

Unpacked files you are working with must be put into `map-<mapname>_<mapversion>.pk3dir` directory,
otherwise game will not find them.
