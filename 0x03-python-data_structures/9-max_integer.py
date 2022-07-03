#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    small = my_list[0]
    for i in my_list:
        if small < i:
            small = i
    return small
