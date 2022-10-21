#!/usr/bin/python3
"""Algorithms for list of integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if list_of_integers:
        sorted(list_of_integers, reverse=True)
        return list_of_integers[0]
