Unvanquished support for TrenchBroom
====================================

Installation
------------

TrenchBroom is not yet usable for Unvanquished, but if you're a developer you can be interested in the game file for testing purpose.

Download the [game directory](games/Unvanquished) and put it in `app/resources/games/` directory within TrenchBroom one.

Using
-----

Set the engine path in TrenchBroom preferences.

Keep in mind game directory must contain `pkg` directory (like `baseq3` was in Quake 3 dir).

Unvanquished has advanced file layout for maps and resources. Every map resides in separate .dpk.
Filename must obey the rule: `map-<mapname>_<mapversion>.dpk`, eg. `map-station_4.dpk`.
