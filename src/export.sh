#!/bin/sh

# gtkradiant
install -m644 game.xlink ../gtkradiant/game/
cd entities
python3 ent_yaml2new.py > ../../gtkradiant/install/pkg/scripts/entities.def
cd ..

# netradiant
install -m644 game.xlink ../netradiant/unvanquished.game/

