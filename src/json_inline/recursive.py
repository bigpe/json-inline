import json
from functools import reduce
from typing import Union

from .search import search_in_list


def fetch(json_data: Union[dict, list], entrypoint_rule: Union[list, str]):
    if isinstance(entrypoint_rule, str):
        entrypoint_rule = entrypoint_rule.split('.')
    new_map_list = entrypoint_rule[:]
    if isinstance(json_data, str):
        try:
            json_data = json.loads(json_data)
        except json.JSONDecodeError:
            if not len(entrypoint_rule):  # All moves passed
                return json_data
            return None  # Move not finish
    new_data = json_data
    if not new_map_list:
        return new_data
    if isinstance(json_data, dict):
        new_data, new_map_list = recursive_dict(json_data, entrypoint_rule)
    if isinstance(json_data, list):
        # Search Modificator
        if new_map_list[0][0] == '?':
            new_data, new_map_list = search_in_list(new_data, new_map_list)
        else:
            new_data, new_map_list = recursive_list(json_data, entrypoint_rule)
    if new_map_list == entrypoint_rule:
        return new_data
    return fetch(new_data, new_map_list)


def recursive_dict(data: dict, entrypoint_rule: list):
    new_map_list = []
    temp_map_list = entrypoint_rule
    for i, m in enumerate(entrypoint_rule):
        if str(m)[0] == '#':
            m = m.replace('#', '', 1)
        if type(m) == int or m.isdigit() or m[0] == '?':
            temp_map_list = temp_map_list[i:]
            break
        new_map_list.append(m)
    new_data = reduce(dict.get, new_map_list, data)
    return new_data, temp_map_list


def recursive_list(data: list, entrypoint_rule: list):
    new_map_list = []
    for i, m in enumerate(entrypoint_rule):
        if str(m)[0] == '#':
            m = m.replace('#', '', 1)
        try:
            m = int(m)
        except ValueError:
            ...
        if type(m) != int:
            entrypoint_rule = entrypoint_rule[i:]
            break
        new_map_list.append(m)
    for m in new_map_list:
        try:
            data = data[m]
        except IndexError:
            data = None
    return data, entrypoint_rule

