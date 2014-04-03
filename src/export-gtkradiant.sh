#!/bin/sh

cd $( dirname $0 )

ROOT="../gtkradiant"

install -m644 game.xlink "${ROOT}/game/"
python3 entities/ent_yaml2new.py --generate --dummyflag --yamlname entities/entities.yaml\
    > "${ROOT}/install/pkg/scripts/entities.def"
