#!/bin/sh

ROOT="../netradiant"

mkdir -p "${ROOT}/unvanquished.game/pkg"
install -m644 game.xlink "${ROOT}/unvanquished.game/"
python3 entities/ent_yaml2new.py entities/entities.yaml > "${ROOT}/unvanquished.game/pkg/entities.def"
