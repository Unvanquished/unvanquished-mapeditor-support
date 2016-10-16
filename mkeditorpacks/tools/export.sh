#! /bin/sh

cd "$(dirname "${0}")"

SRC='../src'
GTKRADIANT='../build/gtkradiant'
NETRADIANT='../build/netradiant'
SETTINGS="${SRC}/settings.ini"

printHelp () {
	tab="$(printf '\t')"

	cat <<-EOF
	usage: ${0} [option]

	option:
	${tab}-h, --help
	${tab}${tab}print this help
	${tab}-g, --gtkradiant
	${tab}${tab}build GtkRadiant gamepack
	${tab}-n, --netradiant
	${tab}${tab}build NetRadiant gamepack

	EOF

	exit
}

sanitizeIni () {
	sed -e 's/;.*//;s/^[ ]*\([^ ][^ ]*\)[ ][ ]*=[ ][ ]*\(.*\)*[ ]*$/\1=\2/;s/^\([^ ][^ ]*\)="\(.*\)"/\1=\2/' | grep -v '^$'
}

readIni () {
	ini_file="${1}"
	ini_key="${2}"

	if ! [ -f "${1}" ]
	then
		echo "ERROR: missing ini file"
		exit 1
	fi

	sanitizeIni < ${ini_file} \
	| grep "^${ini_key}=" \
	| head -n 1 \
	| sed -e 's/[^=]*[^=]=//'
}

gamename="$(readIni "${SETTINGS}" 'gamename')"
basegame="$(readIni "${SETTINGS}" 'basegame')"
entities="$(readIni "${SETTINGS}" 'entities')"

if [ -z "${gamename}" ]
then
	echo "ERROR: missing gamename ini key"
	exit 1
fi

if [ -z "${basegame}" ]
then
	echo "ERROR: missing basegame ini key"
	exit 1
fi

if [ -z "${entities}" ]
then
	echo "ERROR: missing entities ini key"
	exit 1
fi

buildForEditor () {
	editor_name="${1}"

	case ${editor_name} in
		'gtkradiant')
			xlink_dir="${GTKRADIANT}/game"
			entities_dir="${GTKRADIANT}/install/${basegame}/scripts"
			buildmenu_option="--gtkradiant"
			buildmenu_dir="${GTKRADIANT}/install/${basegame}/scripts"
			buildmenu_file='default_project.proj'
			shaderlist_dir="${GTKRADIANT}/install/${basegame}/scripts"
			synapse_dir="${GTKRADIANT}/game"
		;;
		'netradiant')
			xlink_dir="${NETRADIANT}/${gamename}.game/"
			entities_dir="${NETRADIANT}/${gamename}.game/${basegame}"
			buildmenu_option="--netradiant"
			buildmenu_dir="${NETRADIANT}/${gamename}.game"
			buildmenu_file="default_build_menu.xml"
			shaderlist_dir="${NETRADIANT}/install/${basegame}"
			games_dir="${NETRADIANT}/games"
			game_file="${gamename}.game"
		;;
	esac

	mkdir --verbose --parents "${xlink_dir}"
	cp --verbose "${SRC}/xlink/game.xlink" "${xlink_dir}/game.xlink"

	mkdir --verbose --parents "${shaderlist_dir}"
	cp --verbose "${SRC}/shaderlist/shaderlist.txt" "${shaderlist_dir}/default_shaderlist.txt"

	mkdir --verbose --parents "${entities_dir}"
	case "${entities}" in
		'yaml')
			echo "entities.py >>>> '${entities_dir}/entities.def'"
			./entities.py -gdTDRE -p "${SRC}/entities/header.txt" "${SRC}/entities/entities.yaml" > "${entities_dir}/entities.def"
		;;
		'def')
			cp --verbose "${SRC}/entities/entities.def" "${entities_dir}/entities.def"
		;;
	esac

	mkdir --verbose --parents "${buildmenu_dir}"
	echo "buildmenu.py >>>> '${buildmenu_dir}/${buildmenu_file}'"
	./buildmenu.py "${buildmenu_option}" "${SRC}/buildmenu/buildmenu.yaml" > "${buildmenu_dir}/${buildmenu_file}"

	case ${editor_name} in
		'gtkradiant')
			mkdir --verbose --parents "${synapse_dir}"
			cp --verbose "${SRC}/synapse/synapse.config" "${synapse_dir}/synapse.config"
		;;
		'netradiant')
			mkdir --verbose --parents "${games_dir}"
			cp --verbose "${SRC}/gamefile/file.game" "${games_dir}/${game_file}"
		;;
	esac
}

enable_gtkradiant=false
enable_netradiant=false

if [ -z "${@}" ]
then
	echo "ERROR: missing option"
	echo ""
	printHelp
fi

for arg in ${@}
do
	case "${arg}" in
		'-g'|'--gtkradiant')
			enable_gtkradiant=true
		;;
		'-n'|'--netradiant')
			enable_netradiant=true
		;;
		'-h'|'--help')
			printHelp
		;;
		*)
			echo "ERROR: bad option"
			echo ""
			printHelp
		;;
	esac
done

if "${enable_gtkradiant}"
then
	buildForEditor 'gtkradiant'
fi

if "${enable_netradiant}"
then
	buildForEditor 'netradiant'
fi

#EOF
