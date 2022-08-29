#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    listLen = len(my_list)
    if idx >= listLen or idx < 0:
        return my_list
    for i in range(listLen):
        if i == idx:
            my_list[i] = element
    return my_list
