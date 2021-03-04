Unvanquished support for GtkRadiant
===================================

Installation
------------

GtkRadiant automatically fetches gamepacks it supports, you have no need to clone this repository.

Prefer using NetRadiant because it provides a better Unvanquished support. If NetRadiant does not work for you GtkRadiant is a good fallback though.

Set the [UnvanquishedAssets](https://github.com/UnvanquishedAssets/UnvanquishedAssets) repository as engine path in GtkRadiant preferences, set `pkg` as `fs_game` and `src` as `fs_game_base`.

Using
-----

During the first start GtkRadiant tries to install additional files into your game directory.
Make sure it's writable for you.

Unvanquished has advanced file layout for maps and resources. Every map resides in separate .dpk.
Filename must obey the rule: `map-<mapname>_<mapversion>.dpk`, eg. `map-station_4.dpk`.

Unpacked files you are working with must be put into `map-<mapname>_<mapversion>.dpkdir` directory,
otherwise game will not find them.

Those are usually stored in a `pkg` directory, or a `src` directory when working with asset sources.