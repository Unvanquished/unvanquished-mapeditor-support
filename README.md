mapeditor-support
=================

Unvanquished support files for map editors.

Using the support files
-----------------------

Pick the directory corresponding to your editor and merge the file hierarchy into its installation. You might need to adjust pathes inside the configuration files depending on your operating system and Unvanquished installation.

Packages
--------

Packages are available for

* [Archlinux & Netradiant](https://aur.archlinux.org/packages/netradiant-unvanquished/)

Contributing
------------

The `src` directory contains common files, source files and export scripts that populate the eidtor specific directories. Files that aren't editor-specific should be maintained there. Ideally we will be able to auto-generate the entire contents of the editor directories eventually.
