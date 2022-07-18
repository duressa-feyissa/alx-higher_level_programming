#!/usr/bin/python3
def safe_print_integer(value):
    hold = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        hold = False
    return hold
