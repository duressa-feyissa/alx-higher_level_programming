#!/usr/bin/python3


def magic_string():
    """
    returns a string “BestSchool” n times the number of the iteration
    """
    try:
        magic_string.counter += 1
    except AttributeError:
        magic_string.counter = 1
    if magic_string.counter == 1:
        return "BestSchool"
    else:
        string = "BestSchool, " * (magic_string.counter - 1)
        string += "BestSchool"
        return string
