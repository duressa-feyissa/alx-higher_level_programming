#!/usr/bin/python3

def islower(c):
    """ A function that checks for lowercase character.

    Args:
        c: character

    Returns:
        True if c is lowercase otherwise False
    """

    if ord(c) >= 97 and ord(c) < 123:
        return True
    else:
        return False
