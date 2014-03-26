import yaml
from collections import OrderedDict

def dict_representer(dumper, data):
    value = [{key : value} for key, value in data.items()]
    old = dumper.default_flow_style
    dumper.default_flow_style = False
    node = dumper.represent_sequence('tag:yaml.org,2002:omap', value)
    dumper.default_flow_style = old
    return node

yaml.add_representer(OrderedDict, dict_representer)

class UnsortableOrderedDict(OrderedDict):
    pass

def represent_mapping(dumper, tag, mapping, flow_style=None):
    value = []
    node = yaml.nodes.MappingNode(tag, value, flow_style=flow_style)
    if dumper.alias_key is not None:
        dumper.represented_objects[dumper.alias_key] = node
    best_style = True
    if hasattr(mapping, 'items'):
        mapping = list(mapping.items())
    for item_key, item_value in mapping:
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)
        if not (isinstance(node_key, yaml.nodes.ScalarNode) and not node_key.style):
            best_style = False
        if not (isinstance(node_value, yaml.nodes.ScalarNode) and not node_value.style):
            best_style = False
        value.append((node_key, node_value))
    if flow_style is None:
        if dumper.default_flow_style is not None:
            node.flow_style = dumper.default_flow_style
        else:
            node.flow_style = best_style
    return node


def represent_dict(dumper, data):
    return represent_mapping(dumper, 'tag:yaml.org,2002:map', data)

yaml.add_representer(UnsortableOrderedDict, represent_dict)

class OpenedDict(dict):
    pass

def odict_repr(dumper, data):
    old = dumper.default_flow_style
    dumper.default_flow_style = False
    node = dumper.represent_dict(data)
    dumper.default_flow_style = old
    return node


yaml.add_representer(OpenedDict, odict_repr)

class ListOfPairs(list):
    pass

def lop_repr(dumper, data):
    value = [{key : value} for key, value in data]
    old = dumper.default_flow_style
    dumper.default_flow_style = False
    node = dumper.represent_sequence('tag:yaml.org,2002:seq', value)
    dumper.default_flow_style = old
    return node

yaml.add_representer(ListOfPairs, lop_repr)
