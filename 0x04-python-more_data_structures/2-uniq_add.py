#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Sum unique element in a list"""
    uniq_list = set(my_list)
    sum = 0
    for i in uniq_list:
        sum += i
    return sum
