.DEFAULT_GOAL := all

export ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
export BUILD_DIR := ${ROOT_DIR}/build

clean:
	rm -Rf ${BUILD_DIR}

all:
	./mkeditorpacks/mkeditorpacks all

darkradiant:
	./mkeditorpacks/mkeditorpacks darkradiant

gtkradiant:
	./mkeditorpacks/mkeditorpacks gtkradiant

jackhammer:
	./mkeditorpacks/mkeditorpacks jackhammer

netradiant:
	./mkeditorpacks/mkeditorpacks netradiant

trenchbroom:
	./mkeditorpacks/mkeditorpacks trenchbroom

