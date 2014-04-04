#!/bin/sh

cd $( dirname $0 )

ROOT="../gtkradiant"

install -m644 game.xlink "${ROOT}/game/"
./entities/ent_yaml2new.py -g -d -p entities/header.txt entities/entities.yaml > "${ROOT}/install/pkg/scripts/entities.def"
