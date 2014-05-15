#!/bin/sh

cd $( dirname $0 )

ROOT="../netradiant/gamepack"

mkdir -p "${ROOT}/unvanquished.game/pkg"
install -m644 game.xlink "${ROOT}/unvanquished.game/"
./entities/ent_yaml2new.py -gdTDRE -p entities/header.txt entities/entities.yaml > "${ROOT}/unvanquished.game/pkg/entities.def"
