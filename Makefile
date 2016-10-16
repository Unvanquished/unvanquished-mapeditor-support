export ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
export SRC_DIR:=${ROOT_DIR}/src
export BUILD_DIR:=${ROOT_DIR}/build

all:
	$(MAKE) -C mkeditorpacks
