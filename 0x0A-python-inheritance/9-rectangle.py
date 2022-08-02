#!/usr/bin/python3
"""
    BaseGeometry Class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle inerits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        initiaitazation
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        area calculate
        """
        return self.__width * self.__height

    def __str__(self):
        """
        __str__ magic function
        """
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
