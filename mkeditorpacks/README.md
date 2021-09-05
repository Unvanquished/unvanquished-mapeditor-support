MkEditorPacks
=============

This a tool set to build game packs for map editors.

It is developped for the [Unvanquished](https://unvanquished.net) project, but must fit any project supported by the editors listed below.

Supported editors
-----------------

- [GtkRadiant](http://icculus.org/gtkradiant)
- [NetRadiant](https://gitlab.com/xonotic/netradiant)
- [DarkRadiant](https://www.darkradiant.net)

Work in progress editor support
-------------------------------

- [J.A.C.K.](http://jack.hlfx.ru/en/main.html)
- [TrenchBroom](http://kristianduske.com/trenchbroom)

Supported output formats
------------------------

### Entity definition file

Editor|NetRadiant `.ent`|Worldcraft `.fgd`|Quake 3 `.def`|Doom 3 `.def`
---|---|---|---|---
NetRadiant|✅| |✅|✅
GtkRadiant| | |✅|
DarkRadiant| | | |✅
J.A.C.K.| |✅| |
TrenchBroom| | |✅|

### Build menu file

Editor|NetRadiant `default_build_menu.xml`|GtkRadiant `default_project.proj`
---|---|---
NetRadiant|✅|
GtkRadiant| |✅

### Game definition file

Editor|NetRadiant `name.game`|DarkRadiant `name.game`|GtkRadiant `synapse.config`|TrenchBroom `GameConfig.cfg`
---|---|---|---|---
NetRadiant|✅| | |
DarkRadiant| |✅| |
GtkRadiant| | |✅|
TrenchBroom| | | |✅

### Help menu file

Editor|GtkRadiant `game.xlink`
---|---
NetRadiant|✅
GtkRadiant|✅
