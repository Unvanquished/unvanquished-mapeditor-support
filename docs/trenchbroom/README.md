Unvanquished support for TrenchBroom
====================================

Installation
------------

TrenchBroom is not yet usable for Unvanquished, but if you're a developer you can be interested by the game file for testing purpose.

Download the [game directoru](games/Unvanquished) and put it in `app/resources/games/` directory within TrenchBroom one.

Using
-----

Set the engine path in TrenchBroom preferences.

Keep in mind game directory must contain `pkg` directory (like `baseq3` was in Quake 3 dir).

Unvanquished has advanced file layout for maps and resources. Every map resides in separate .pk3.
Filename must obey the rule: `map-<mapname>_<mapversion>.pk3`, eg. `map-station_4.pk3`.
