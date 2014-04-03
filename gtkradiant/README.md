Unvanquished support for GtkRadiant
===================================

Supported versions
------------------

* GtkRadiant 1.6

Installation
------------

GtkRadiant automatically fetches gamepacks it supports.
List of available games hardcoded, so you will need patching.
(To get rid of patching sources, I've opened issue: https://github.com/TTimo/GtkRadiant/issues/259)

1. Apply `GtkRadiant.patch`.

        cd GtkRadiant
        patch -p1 < GtkRadiant.patch

2. Compile radiant as usual. This will automatically take the rest of Unvanquished gamepack from repository.

Using
-----

During the first start Radiant tries to install additional files into your game installation directory.
If you have writing rights here, there will be no problem.

If your system makes game installations read-only, you have to work around this. There are 2 possible ways here:
temporarily grant writing to game directory, or start in any other directory and copy .pk3 files here.

Keep in mind that inside game directory must be `pkg` directory (like `baseq3` was in Quake 3 dir).

Unvanquished has advanced file layout for maps and resources. Every map resides in separate .pk3.
Filename must obey the rule: `map-<mapname>_<mapversion>.pk3`, eg. `map-station_4.pk3`.

Unpacked files you are working with must be put into `map-<mapname>_<mapversion>.pk3dir` directory,
otherwise game will not find them.
