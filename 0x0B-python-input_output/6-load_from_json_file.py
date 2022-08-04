#!/usr/bin/python3
"""
   6-load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """
    append
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file.read())
