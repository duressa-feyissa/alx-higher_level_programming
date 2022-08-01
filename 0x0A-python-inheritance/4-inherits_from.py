#!/usr/bin/python3
"""
    4-inherits_from: inherits_from()
"""


def inherits_from(obj, a_class):
    """
        check for class inheritance.
    """

    if not type(obj) is a_class and  issubclass(type(obj), a_class):
        return True
    return False
