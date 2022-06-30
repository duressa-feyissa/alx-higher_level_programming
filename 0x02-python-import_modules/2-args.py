#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    argc = len(argv) - 1
    if argc == 0:
        print("{0:d} arguments.".format(argc))
    else:
        print("{0:d} arguments:".format(argc))
        for i in range(1, argc + 1):
            print("{0:d}: {1:s}".format(i, argv[i]))
