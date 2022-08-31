#!/usr/bin/python3

def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets."""
    # first approach
    # common_set = set_1 & set_2

    # second approach
    # common_set = set_1.intersection(set_2)

    # third approach
    # common_set = []
    # for i in set_1:
    #     for j in set_2:
    #         if i == j:
    #             common_set.append(i)

    # fourth approach
    # common_set = set()
    # for x in set_1:
    #     if x in set_2:
    #         common_set.add(x)

    # fifth approach
    common_set = set()
    [common_set.add(x) for x in set_1 if x in set_2]
    return common_set
