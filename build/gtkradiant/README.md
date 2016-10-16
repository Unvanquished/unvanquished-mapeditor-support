Unvanquished support for GtkRadiant
===================================

Installation
------------

GtkRadiant automatically fetches gamepacks it supports, you have no need to clone this repo.

List of available games is hardcoded, so GtkRadiant must be patched in order to support Unvanquished. Some work have been started but nothing is usable yet and development stopped. If you have the skill, join [#unvanquished on freenode](http://webchat.freenode.net/?channels=%23unvanquished) to get more information. Prefer using NetRadiant currently.

Using
-----

During the first start Radiant tries to install additional files into your game directory.
Make sure it's writable for you.

Keep in mind game directory must contain `pkg` directory (like `baseq3` was in Quake 3 dir).

Unvanquished has advanced file layout for maps and resources. Every map resides in separate .pk3.
Filename must obey the rule: `map-<mapname>_<mapversion>.pk3`, eg. `map-station_4.pk3`.

Unpacked files you are working with must be put into `map-<mapname>_<mapversion>.pk3dir` directory,
otherwise game will not find them.
