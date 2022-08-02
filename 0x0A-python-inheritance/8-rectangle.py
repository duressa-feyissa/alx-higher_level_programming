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
