#!/usr/bin/python3
"""
   1-write_file.py
"""


def write_file(filename="", text=""):
    """
    write
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
