#!/usr/bin/python3
"""
contains a class Base.
"""
import json


class Base():
    """
    base class for the entire project.
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """
        Initializes the class attributes.
        """
        if id is not None:
            self.id =id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON string repr of list_dictionaries
        """
        if len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)
