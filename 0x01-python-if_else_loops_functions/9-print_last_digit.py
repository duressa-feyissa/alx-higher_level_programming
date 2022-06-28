#!/usr/bin/env python3


def print_last_digit(number):
    """ A function that prints the last digit of a number.

    Args:
        number: value

    Returns:
        last digit
    """
    last_digit = abs(number) % 10
    print("{0:d}".format(last_digit), end="")
    return last_digit
