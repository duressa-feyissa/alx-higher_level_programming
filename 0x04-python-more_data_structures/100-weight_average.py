#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0

    add = 0
    count = 0
    for i in my_list:
        hold = tuple(i)
        add += hold[0] * hold[1]
        count += hold[1]
    return add / count
