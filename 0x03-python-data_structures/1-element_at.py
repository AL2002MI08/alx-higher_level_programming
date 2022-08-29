#!/usr/bin/python3
def element_at(my_list, idx):
    """Return element at index (idx)"""
    listLen = len(my_list)
    if idx >= listLen or idx < 0:
        return None
    for i in range(listLen):
        if i == idx:
            return my_list[i]
