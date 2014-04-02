Unvanquished support for GtkRadiant
===================================

Supported versions
------------------

* GtkRadiant 1.6

Installation
------------

This gamepack requires patching GtkRadiant. Download `GtkRadiant.patch` and run this before compiling the source:

	cd GtkRadiant
	patch -p1 < GtkRadiant.patch

<!--
Run scons (this will automatically checkout this repo into your GtkRadiant/install):

	scons
-->

In order for entitiy models to appear correctly, you need to copy `unvanquished_*.pk3` from the `pkg` subfolder of your Unvanquished installation into `~/.unvanquished/pkg/`.
<!-- Viech: Your package must locate the global Unvanquished files! Making the user copy the entire unvanquished installation is not an option, especially not when we add texture packages. -->

When you run radiant there will be a setup dialog. Choose Unvanquished and point its gamedir to `~/.unvanquished/`.
<!-- Viech: The manual configuration of the home directory shouldn't be necessary. Use this to make the user point to the installation directory instead! (See my comment above.) -->

In order to switch the map you are currently editing, use the `mapselect.sh` script:

	cd ~/.unvanquished/pkg/
	chmod +x mapselect.sh
	./mapselect <newmap>
<!-- Viech: The user shouldn't really be required to do this. Especially since the support package needs to run on windows, too.
     Try to figure out a way that doesn't involve installing additional programs/scripts.
     Also, if possible, don't require the user to manually place stuff inside pathes belonging to Unvanquished. -->
