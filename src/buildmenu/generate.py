#!/usr/bin/env python3

import yaml
import re
import sys
import os.path
from xml.etree import ElementTree as ET
from datetime import datetime
import argparse

opt_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'options.yaml')


def fine_format_xml(root):
    lines = ET.tostringlist(root, encoding='unicode')
    result = []
    prev = '>'
    for line in lines:
        if (line.startswith('<') and prev.endswith('>')) and not (line.startswith('</var>') and prev.endswith('</cond>')):
            result.append('\n')
        result.append(line)
        prev = line
    return ''.join(result)


def sort_stage_keys(stage):
    result = []
    for k, v in stage:
        if k in ('meta', 'vis', 'light', 'minimap'):
            result.insert(0, (k, v))
        else:
            result.append((k, v))
    return result


def print_gtkradiant_file(data):
    project = ET.Element('project')

    def add(name, value):
        value = str(value)
        value = value.replace('@', '$TEMPLATE')
        ET.SubElement(project, 'key', attrib={'name': name, 'value': value})

    add('version', 2)
    d = datetime.utcnow()
    tv = d.day + d.month * 32 + (d.year - 2000) * 367
    add('template_version', tv) # increase every update
    add('basepath', '@enginepath@basedir/')
    add('rshcmd', '')
    add('entitypath', '@toolspath@basedir/scripts/entities.def')
    add('texturepath', '@enginepath@basedir/textures/')
    add('autosave', '@userhomepath@basedir/maps/autosave.map') # bad. should be replaced
    add('mapspath', '@userhomepath@basedir/maps/') # bad. should be replaced

    for cmd in data:
        name = 'bsp_Q3Map2: ' + cmd['name']
        stagelist = []
        for stage in cmd['opts']:
            olist = [
                '"@apppath@q3map2"',
                '-v',
                '#',
                '-game unvanquished',
                '-fs_basepath "@enginepath"',
            ]
            for o, v in sort_stage_keys(stage.items()):
                t = '-' + o
                if v is not None:
                    t += ' {}'.format(v)
                olist.append(t)
            olist.append('$')
            stagelist.append(' '.join(olist))
        value = '! ' + ' && ! '.join(stagelist)
        add(name, value)


    print('<?xml version="1.0"?>')
    print('<!DOCTYPE project SYSTEM "dtds/project.dtd">')
    print(fine_format_xml(project))


def print_netradiant_file(data):
    project = ET.Element('project', attrib={'version': '2.0'})

    q3map2 = ET.SubElement(project, 'var', attrib={'name': 'q3map2'})
    q3map2.text = '"[RadiantPath]q3map2.[ExecutableType]" -v'
    cond = ET.SubElement(q3map2, 'cond', attrib={'value': '[MonitorAddress]'})
    cond.text = ' -connect [MonitorAddress]'
    cond.tail = ' -game unvanquished -fs_basepath "[EnginePath]" -fs_homepath "[UserEnginePath]" '
    cond2 = ET.SubElement(q3map2, 'cond', attrib={'value': '[GameName]'})
    cond2.text = ' -fs_game [GameName]'

    for cmd in data:
        build = ET.SubElement(project, 'build', attrib={'name': cmd['name']})
        for stage in cmd['opts']:
            olist = ['[q3map2]']
            for o, v in sort_stage_keys(stage.items()):
                t = '-' + o
                if v is not None:
                    t += ' {}'.format(v)
                olist.append(t)
            olist.append('"[MapFile]"')

            command = ET.SubElement(build, 'command')
            command.text = ' '.join(olist)

    print('<?xml version="1.0"?>')
    print(fine_format_xml(project))


def create_parser():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Generates radiant q3map2 build menu file.')

    group = parser.add_argument_group(title='Radiant')
    group = group.add_mutually_exclusive_group(required=True)
    group.add_argument('-n', '--net', action='store_true', help='NetRadiant')
    group.add_argument('-g', '--gtk', action='store_true', help='GtkRadiant')

    return parser

args = create_parser().parse_args()

with open(opt_filename, 'r') as f:
    text = f.read()
    data = yaml.load(text)

    if args.net:
        print_netradiant_file(data)
    elif args.gtk:
        print_gtkradiant_file(data)
