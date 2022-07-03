#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return None
    new_list = list(my_list)
    for i in range(len(new_list)):
        if i == idx:
            new_list[i] = element
            return new_list
    else:
        return None
