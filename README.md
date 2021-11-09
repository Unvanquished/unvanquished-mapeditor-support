unvanquished-mapeditor-support
==============================

Unvanquished support files for map editors.

**These packages are work in progress!**


Using the support files
-----------------------

Pick the directory corresponding to your editor and merge the file hierarchy inside the `gamepack` subdirectory into its installation. Further installation instructions are given in a seperate per-editor readme file.

* [NetRadiant](build/netradiant/README.md) ★★★★★ _(preferred and recommended)_
* [GtkRadiant](build/gtkradiant/README.md) ★★★ _(serious fallback)_
* [DarkRadiant](build/darkradiant/README.md) ★★★ _(serious fallback)_
* [J.A.C.K.](build/jackhammer/README.md) ★ _(some managed to do something with it)_
* [~~TrenchBroom~~](build/trenchbroom/README.md) _(not yet usable)_

> **Note:** _The `NetRadiant-custom` fork by Garux does not work with Unvanquished because it lacks most of the required features implemented upstream since 2014. The gamepack provided with NetRadiant-custom is obsolete and will not work but using an up-to-date gamepack instead will not work either because of features being missing to begin with._

Contributing
------------

It can sound obvious, but the `src` directory contains source files. The `build` directory contains the generated files. Do not modify files in `build` directories or your changes will be overwritten.
