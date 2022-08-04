#!/usr/bin/python3
""" Student class
"""


class Student():
    """class
    """

    def __init__(self, first_name, last_name, age):
        """initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """  retrieves a dictionary
        """
        if isinstance(attrs, list):
            new = dict()
            if "first_name" in attrs:
                new["first_name"] = self.first_name
            if "last_name" in attrs:
                new["last_name"] = self.last_name
            if "age" in attrs:
                new["age"] = self.age
            return new
        return self.__dict__

    def reload_from_json(self, json):
        """
        json (dictionary): reload data.
        """
        for key, value in json.items():
            self.__setattr__(key, value)
