#!/usr/bin/python3
"""
    BaseGeometry Class
"""


class BaseGeometry():
    """
        empty class
    """

    def area(self):
        """
        Area
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    class Rectangle
    """

    def __init__(self, width, height):
        """
        initiaitazation
        """
        self.integer_validator(width, width)
        self.__width = width
        self.integer_validator(height, height)
        self.__height = height
