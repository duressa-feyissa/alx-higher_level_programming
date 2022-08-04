#!/usr/bin/python3
"""
   2-write_file.py
"""
import json


def save_to_json_file(my_obj, filename):
    """
    write
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(json.dumps(my_obj))
