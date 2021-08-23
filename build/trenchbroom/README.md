Unvanquished support for TrenchBroom
====================================

Installation
------------

[TrenchBroom](https://kristianduske.com/trenchbroom/) is not yet usable for Unvanquished, but if you're a developer you can be interested in the game file for testing purpose.

Download the [game directory](games/Unvanquished) and put it in `app/resources/games/` directory within TrenchBroom one.

Using
-----

Set the engine path in TrenchBroom preferences.

Unvanquished has advanced file layout for maps and resources. Every map resides in separate .dpk.
Filename must obey the rule: `map-<mapname>_<mapversion>.dpk`, eg. `map-station_4.dpk`.

Those are usually stored in a `pkg` directory, or a `src` directory when working with asset sources.
