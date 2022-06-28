#!/usr/bin/python3
def print_last_digit(number):
    """ A function that prints the last digit of a number.

    Args:
        number: value

    Returns:
        last digit
    """
    if number >= 0:
        last_digit = number % 10
    else:
        last_digit = (number * -1) % 10
    print(last_digit, end="")
    return last_digit
