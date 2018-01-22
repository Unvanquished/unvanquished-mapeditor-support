.DEFAULT_GOAL := all

export ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
export SRC_DIR:=${ROOT_DIR}/src
export BUILD_DIR:=${ROOT_DIR}/build

clean:
	rm -Rf ${BUILD_DIR}

all:
	$(MAKE) -C mkeditorpacks all

darkradiant:
	$(MAKE) -C mkeditorpacks darkradiant

gtkradiant:
	$(MAKE) -C mkeditorpacks gtkradiant

jackhammer:
	$(MAKE) -C mkeditorpacks jackhammer

netradiant:
	$(MAKE) -C mkeditorpacks netradiant
