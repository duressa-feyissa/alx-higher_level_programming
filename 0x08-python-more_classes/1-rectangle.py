#!/usr/bin/python3
""" Module contains empty class Rectangle """


class Rectangle:
    """ empty class """

    def __init__(self, width=0, height=0):
        """ initilaizier """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """  to retrieve it """
        return self.__width

    @width.setter
    def width(self, value):
        """ to set it """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """  to retrieve it """
        return self.__height

    @height.setter
    def height(self, value):
        """  to set it  """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
