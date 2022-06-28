#!/usr/bin/python3

for i in range(122, 96, -1):
    if (i % 2 == 0):
        hold = i
    else:
        hold = i - 32
    print("{0:c}".format(hold), end="")
