#!/bin/sh

# gtkradiant
install -m644 game.xlink ../gtkradiant/game/
python3 entities/ent_yaml2new.py entities/entities.yaml > ../gtkradiant/install/pkg/scripts/entities.def

# netradiant
install -m644 game.xlink ../netradiant/unvanquished.game/
mkdir -p ../netradiant/unvanquished.game/main/
python3 entities/ent_yaml2new.py entities/entities.yaml > ../netradiant/unvanquished.game/main/entities.def
