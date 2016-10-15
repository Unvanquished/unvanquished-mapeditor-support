mapeditor-support
=================

Unvanquished support files for map editors.

**These packages are work in progress!**

Using the support files
-----------------------

Pick the directory corresponding to your editor and merge the file hierarchy inside the `gamepack` subdirectory into its installation. Further installation instructions are given in a seperate per-editor readme file.

* [GtkRadiant readme](gtkradiant/README.md)
* [NetRadiant readme](netradiant/README.md)

Packages
--------

Packages are available for

* [Archlinux & Netradiant](https://aur.archlinux.org/packages/netradiant-unvanquished-git/)

Contributing
------------

The `src` directory contains common files, source files and export scripts that populate the editor specific directories. Files that aren't editor-specific should be maintained there. Ideally we will be able to auto-generate the entire contents of the editor directories eventually.
