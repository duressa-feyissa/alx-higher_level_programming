#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    sum = 0
    argc = len(argv) - 1
    if argc == 0:
        print("{0:d}".format(sum))
    else:
        for i in range(1, argc + 1):
            sum += int(argv[i])
        print("{0:d}".format(sum))
