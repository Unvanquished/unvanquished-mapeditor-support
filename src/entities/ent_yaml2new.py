#!/usr/bin/env python3

import yaml
import re
import sys
import os.path
import argparse


bad_token_re = re.compile(r'[}{)(\':\s]', re.M)

def escape_token(t):
    if bad_token_re.search(t):
        if t.find('"') >= 0:
            raise Exception('Bad token: {}'.format(t))
        return '"{}"'.format(t)
    return t

def color_to_float_triple(h):
    hexes = [h[:2], h[2:4], h[4:]]
    return [round(int(x, 16) / 255.0, 3) for x in hexes]



def list_of_dicts_to_list_of_tuples(dd):
    res = []
    for d in dd:
        for k, v in d.items():
            res.append((k, v))
            break
    return res


# ==============================================================================
# entity output in native radiant format


# https://github.com/TTimo/GtkRadiant/issues/262
dont_place_dummy_flag = True

heading = '------ {} ------'

def fmt_float(f):
    x = '{:f}'.format(f)
    if 'e' in x:
        return x
    return x.rstrip('0').rstrip('.')

def _output_float(v):
    return fmt_float(v)

def _output_vec2_float(v):
    return ' '.join(_output_float(vv) for vv in v)

def _output_vec3_float(v):
    return ' '.join(_output_float(vv) for vv in v)

def _output_vec4_float(v):
    return ' '.join(_output_float(vv) for vv in v)

def outvalue(v, _type):
    func_name = '_output_' + _type
    if _type is None or func_name not in globals():
        return str(v)
    return globals()[func_name](v)

def print_entity_head(e):
    name = escape_token(e['name'])
    color = '({} {} {})'.format(*(fmt_float(f) for f in color_to_float_triple(e['color'])))
    flags = [escape_token(k) for k, _ in e['flags']]
    if 'size_min' in e and 'size_max' in e:
        sizes = ' ({} {} {}) ({} {} {})'.format(*(fmt_float(f) for f in e['size_min'] + e['size_max']))
    else:
        sizes = ''
        if not dont_place_dummy_flag:
            flags.insert(0, escape_token('?'))
    flags = ' '.join(flags)
    if flags:
        flags = ' ' + flags
    print('/*QUAKED {} {}{}{}'.format(name, color, sizes, flags))


def print_flag_desc(e):
    flags = []
    for k, v in e['flags']:
        if k == '-' or not v:
            continue
        flags.append('{}: {}'.format(k, v))
    if flags:
        print(heading.format('FLAGS'))
        for v in flags:
            print(v)


def print_prop_desc(e, dt, pr_types, pr_defaults, pr_ranges, pr_eg):
    if 'props' not in e or not e['props']:
        return

    print(heading.format('PROPERTIES'))
    proptypes, propdefaults, propranges, propreplace, propeg, boolvalues = \
        (e.get(k, {}) for k in ('proptypes', 'propdefaults', 'propranges', 'propreplace', 'propeg', 'boolvalues'))

    for k, v in sorted(e['props'].items()):
        _type = proptypes[k] if k in proptypes else (dt[k] if k in dt else None)
        _bool = k in boolvalues
        info = []
        if pr_types and _type is not None:
            info.append(_type)
        if pr_eg and k in propeg:
            info.append('eg: {}'.format(outvalue(propeg[k], _type)))
        if pr_ranges and k in propranges:
            v1, v2 = propranges[k]
            info.append('{}..{}'.format(outvalue(v1, _type), outvalue(v2, _type)))
        if pr_ranges and _bool:
            v1, v2 = boolvalues[k]
            info.append('{} or {}'.format(outvalue(v1, _type), outvalue(v2, _type)))
        if pr_defaults and k in propdefaults:
            v1 = propdefaults[k]
            if _bool:
                v1 = boolvalues[k][1 if v1 else 0]
            info.append('def: {}'.format(outvalue(v1, _type)))
        if info:
            info = ' ({})'.format(', '.join(info))
        else:
            info = ''
        if k in propreplace:
            for _from, _to in propreplace[k].items():
                v = v.replace(_from, _to)
        print('{}: {}{}'.format(k, v, info))


def print_common_desc(e):
    if e['desc']:
        print(heading.format('DESCRIPTION'))
        v = e['desc']
        if 'descreplace' in e:
            for _from, _to in e['descreplace'].items():
                v = v.replace(_from, _to)
        print(v)


def print_specials(e):
    if e['specials']:
        for k, v in e['specials'].items():
            print('{}="{}"'.format(k, v))


def print_entity(e, dt, pr_types=False, pr_defaults=False, pr_ranges=False, pr_eg=False):
    print_entity_head(e)
    if e.get('deprecated'):
        print('DEPRECATED! DEPRECATED! DEPRECATED!')
    print_flag_desc(e)
    print_prop_desc(e, dt, pr_types, pr_defaults, pr_ranges, pr_eg)
    print_common_desc(e)
    print_specials(e)
    print('*/')
    print()


# ==============================================================================
# validators


def _validate_int(v):
    return type(v) == int

def _validate_string(v):
    return type(v) == str

def _validate_float(v):
    return type(v) in (int, float)

def _validate_vec2_float(v):
    return isinstance(v, (list, tuple)) and len(v) == 2 and all(_validate_float(x) for x in v)

def _validate_vec3_float(v):
    return isinstance(v, (list, tuple)) and len(v) == 3 and all(_validate_float(x) for x in v)

def _validate_vec4_float(v):
    return isinstance(v, (list, tuple)) and len(v) == 3 and all(_validate_float(x) for x in v)

def _validate_time_2float(v):
    if isinstance(v, (list, tuple)):
        return _validate_vec2_float(v)
    return _validate_float(v)

def _validate_vec2_int(v):
    return isinstance(v, (list, tuple)) and len(v) == 2 and all(_validate_int(x) for x in v)


def canonize_type(t):
    t = str(t)
    if ' ' in t:
        t, _ = t.split(' ', 1)
    return t


def val_fields_exist(e):
    if d:
        re
    return all(
        'name' in e,
        'props' in e
    )

required_fields = {'name', 'color', 'flags', 'props', 'desc', 'specials'}
required_fields2 = required_fields | {'size_min', 'size_max'}
additional_fields = {'propreplace', 'proptypes', 'propdefaults', 'propranges', 'boolvalues', 'propeg'}
all_fields = required_fields2 | additional_fields | {'deprecated', 'descreplace'}

def validate_entity(e, dt):
    r = []

    # required fields presence
    d = required_fields - e.keys()
    if d:
        r.append('No required fields: {}'.format(d))
        return r
    if 'size_min' in e or 'size_max' in e:
        d = required_fields2 - e.keys()
        if d:
            r.append('No required fields: {}'.format(d))
            return r

    # unknown fields
    d = e.keys() - all_fields
    if d:
        r.append('Unknown fields: {}'.format(d))
        return r

    # prop* keys consistency
    props = set(e['props'].keys())
    for k in additional_fields:
        val = set(e.get(k, {}).keys())
        x = val - props
        if x:
            r.append('Non-existent properties ({}) in {}: {}'.format(len(x), k, x))

    boolvalues, propdefaults, propeg, propranges, propreplace, proptypes =\
        (set(e.get(k, {}).keys()) for k in sorted(additional_fields))

    possible_types = proptypes | set(dt.keys())

    # if we have default, we must have known type
    x = propdefaults - possible_types
    if x:
        r.append('Properties ({}) in defaults are not exist in types: {}'.format(len(x), x))

    # if we have value range, we must have known type
    x = propranges - possible_types
    if x:
        r.append('Properties ({}) in ranges are not exist in types: {}'.format(len(x), x))

    # value cannot have range and be bool at the same time
    x = propranges & boolvalues
    if x:
        r.append('Properties ({}) have ranges and boolvalues at the same time: {}'.format(len(x), x))

    etypes = e.get('proptypes', {})

    # validate types
    unknown_types = set()
    for field, ftype in etypes.items():
        ftype = canonize_type(ftype)
        # unknown
        func_name = '_validate_{}'.format(ftype)
        if func_name not in globals():
            unknown_types.add(ftype)
            r.append('Property type {}:{} is unknown'.format(field, ftype))
        # duplicates
        if field in dt and ftype == canonize_type(dt[field]):
            r.append('Property type {}:{} duplicates entry from deftypes'.format(field, ftype))

    # validate types of default values
    for field in propdefaults & possible_types:
        ftype = canonize_type(etypes[field] if field in etypes else dt[field])
        if ftype in unknown_types:
            continue
        func_name = '_validate_{}'.format(ftype)
        v = e['propdefaults'][field]
        if isinstance(v, bool) and field in boolvalues:
            if not isinstance(e['boolvalues'][field], list) or len(e['boolvalues'][field]) != 2:
                r.append('Invalid bool list of prop {}'.format(field))
            else:
                for bv in e['boolvalues'][field]:
                    if not globals()[func_name](bv):
                        r.append('Invalid bool value {} of prop {}, must be of type {}'.format(bv, field, ftype))
        elif not globals()[func_name](v):
            r.append('Invalid default value of {}: {}, must be of type {}'.format(field, v, ftype))

    # validate types of range values
    for field in propranges & possible_types:
        ftype = canonize_type(etypes[field] if field in etypes else dt[field])
        if ftype in unknown_types:
            continue
        func_name = '_validate_{}'.format(ftype)
        v = e['propranges'][field]
        if not isinstance(v, list) or len(v) != 2:
            r.append('Invalid range of prop {}'.format(field))
        else:
            v1, v2 = v
            if not globals()[func_name](v1):
                r.append('Invalid min value of {}: {}, must be of type {}'.format(field, v1, ftype))
            if not globals()[func_name](v2):
                r.append('Invalid max value of {}: {}, must be of type {}'.format(field, v2, ftype))
            # todo: check max>min

    # validate types of examples
    for field in propeg & possible_types:
        ftype = canonize_type(etypes[field] if field in etypes else dt[field])
        if ftype in unknown_types:
            continue
        func_name = '_validate_{}'.format(ftype)
        v = e['propeg'][field]
        if not globals()[func_name](v):
            r.append('Invalid example value of {}: {}, must be of type {}'.format(field, v, ftype))


    if unknown_types:
        r.append('Types ({}) are unknown: {}'.format(len(unknown_types), unknown_types))

    return r


# ==============================================================================
# coverage


def entity_type_coverage(e, dt):
    props = set(e['props'].keys())
    proptypes = set(e.get('proptypes', {}).keys())
    propdefaults = set(e.get('propdefaults', {}).keys())

    t = proptypes | (props & set(dt.keys()))

    if len(t) < len(props):
        print('{}%: {}'.format(len(t) * 100 // len(props), e['name']))


# ==============================================================================
# main


def create_parser():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Generates radiant entity definition files from a yaml input file.')

    group = parser.add_argument_group(title='action')
    group = group.add_mutually_exclusive_group(required=True)
    group.add_argument('-s', '--validate', action='store_true', help='Validate yaml syntax')
    group.add_argument('-g', '--generate', action='store_true', help='Generate entities file')
    group.add_argument('-c', '--coverage', action='store_true', help='Analyse completeness of data')

    parser.add_argument('yamlname', default='entities.yaml', nargs='?', help='Path to input file')
    parser.add_argument('-d', '--dummyflag', action='store_true',
        help='Use in unpatched Radiant: https://github.com/TTimo/GtkRadiant/issues/262')
    parser.add_argument('-p', '--header', help='Prepend a header to the generated file.')

    parser.add_argument('-T', '--gtypes', action='store_true', help='Output types of values')
    parser.add_argument('-D', '--gdefaults', action='store_true', help='Output default values')
    parser.add_argument('-R', '--granges', action='store_true', help='Output possible value ranges')
    parser.add_argument('-E', '--gexamples', action='store_true', help='Output example values')
    return parser

def load_main_file(name):
    with open(name, 'r') as f:
        text = f.read()
        elist = yaml.load(text)
        # autofix data
        for e in elist:
            e['flags'] = list_of_dicts_to_list_of_tuples(e['flags'])
    return elist

def get_deftypes_name(mainname):
    d = os.path.dirname(mainname)
    fname = os.path.basename(mainname).split('.')
    if fname[-1] in ('yaml', 'yml'):
        fname.insert(-1, 'deftypes')
    else:
        fname.append('deftypes')
    return os.path.join(d, '.'.join(fname))

def load_deftypes_file(name):
    if not os.path.isfile(name):
        return {}
    with open(name, 'r') as f:
        text = f.read()
        deftypes = yaml.load(text)
    return deftypes

args = create_parser().parse_args()
elist = load_main_file(args.yamlname)
deftypes = load_deftypes_file(get_deftypes_name(args.yamlname))

dont_place_dummy_flag = not args.dummyflag

if args.validate:
    warns = []
    for e in elist:
        w = validate_entity(e, deftypes)
        w = ['{}: {}'.format(e['name'], line) for line in w]
        warns.extend(w)

    if not warns:
        print('No warinings! File is OK.')
    else:
        for w in warns:
            print(w)
        print('==================')
        print('Warning count: {}'.format(len(warns)))
        exit(1)
elif args.coverage:
    for e in elist:
        entity_type_coverage(e, deftypes)
elif args.generate:
    if args.header:
        with open(args.header, "r") as fp:
            for line in fp.readlines():
                print("// {}".format(line.rstrip()))
        print()
    opts = {
        'pr_types': args.gtypes,
        'pr_defaults': args.gdefaults,
        'pr_ranges': args.granges,
        'pr_eg': args.gexamples,
    }
    for e in elist:
        print_entity(e, deftypes, **opts)
