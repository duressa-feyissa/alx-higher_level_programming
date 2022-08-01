#!/usr/bin/python3
"""
    2-is_same_class: is_same_class()
"""


def is_same_class(obj, a_class):
    """
        is exactly an instance of the specified class
    """

    return type(obj) is a_class
