#!/usr/bin/python3
# base.py
"""
contains a class Base.
"""
import json


class Base:
    """
    base class for the entire project.

    Attributes:
    __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0


    def __init__(self, id=None):
        """
        Initializes the class attributes.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON string repr of list_dictionaries

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        """Write objects to a file.
       `
        Args:
            list_objs (list): A list of dictionaries.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                hold = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(hold))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a rectange/ object
        """

        if not dictionary and dictionary == {}:
            return

        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Loads from file
        """
        try:
            with open(cls.__name__ + ".json", 'r') as json_file:
                objs = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in objs]
        except IOError:
            return []
