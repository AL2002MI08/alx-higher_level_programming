#!/usr/bin/python3

def weight_average(mylist=[]):
    """Return the weighted average of all integers tuple (<score>, <weight>)"""
    if (not isinstance(mylist, list) or len(mylist) == 0):
        return 0

    avg = 0
    size = 0

    for x in mylist:
        avg += (x[0] * x[1])
        size += x[1]
    return (avg / size)
