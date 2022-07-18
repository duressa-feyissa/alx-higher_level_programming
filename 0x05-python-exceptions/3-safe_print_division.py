#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        que = a / b
    except ZeroDivisionError:
        que = None
    finally:
        print("Inside result: {}".format(que))
    return que
