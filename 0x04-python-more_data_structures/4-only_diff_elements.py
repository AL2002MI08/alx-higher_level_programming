#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set"""
    # first approach
    # diff_set = set_1 ^ set_2

    # second approach
    # diff_set = set_1.symmetric_difference(set_2)

    # third approach
    diff_set = set()
    [diff_set.add(x) for x in set_1 if x not in set_2]
    [diff_set.add(y) for y in set_2 if y not in set_1]
    return diff_set
