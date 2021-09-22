""""
You are given a tree-like data structure represented as nested dictionaries.
Implement a function collect_leaves that accepts a tree and returns a list of all its leaves. A leaf is a bottom-most node in a tree.

Implement a kind of unit tests via assert operator.
"""
from typing import Union


def collect_leaves(u: Union[dict, list]):
    flatten_list = []
    if isinstance(u, dict):
        for item in u.values():
            flatten_list.extend(collect_leaves(item))
    else:
        flatten_list.extend(u)
    return flatten_list


tree = {
    "node1": {
        "node11": {
            "node111": [1, 2, 3],
            "node112": [4, 5]
        },
        "node12": [6]
    },
    "node2": [7, 8, 9]
}

assert collect_leaves([1, 2, 3]) == [1, 2, 3]
assert collect_leaves(tree) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
