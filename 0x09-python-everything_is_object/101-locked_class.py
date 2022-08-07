#!/usr/bin/python3
""" 101-locked_class.py
"""


class LockedClass:
    """
    no class or object attribute, that prevents the
    user from dynamically creating new instance attributes
    """
    __slots__ = ['first_name']
