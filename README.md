unvanquished-mapeditor-support
==============================

Unvanquished support files for map editors.

**These packages are work in progress!**

Using the support files
-----------------------

Pick the directory corresponding to your editor and merge the file hierarchy inside the `gamepack` subdirectory into its installation. Further installation instructions are given in a seperate per-editor readme file.


* [NetRadiant](build/netradiant/README.md) ★★★★★ _(preferred and recommended)_
* [GtkRadiant](build/gtkradiant/README.md) ★★★ _(serious fallback)_
* [J.A.C.K.](build/jackhammer/README.md) ★ _(some managed to do something with it)_
* [~~DarkRadiant~~](build/darkradiant/README.md) _(not yet usable)_
* [~~TrenchBroom~~](build/trenchbroom/README.md) _(not yet usable)_

Packages
--------

Packages are available for

* [Archlinux & Netradiant](https://aur.archlinux.org/packages/netradiant-unvanquished-git/)

Contributing
------------

It can sound obvious, but the `src` directory contains source files. The `build` directory contains the generated files. Do not modify files in `build` directories or your changes will be overwritten.
