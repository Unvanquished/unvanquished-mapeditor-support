#!/bin/sh

ROOT="../gtkradiant"

install -m644 game.xlink "${ROOT}/game/"
python3 entities/ent_yaml2new.py entities/entities.yaml > ${ROOT}/install/pkg/scripts/entities.def
