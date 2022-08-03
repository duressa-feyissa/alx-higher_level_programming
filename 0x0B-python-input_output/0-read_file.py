#!/usr/bin/python3
"""
0-read_file.py
"""


def read_file(filename=""):
    """
    read file my_file_0.txt
    """
    with open("my_file_0.txt") as file:
        for i in file:
            print(i, end="")
