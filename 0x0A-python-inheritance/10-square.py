#!/usr/bin/python3
"""
    Square Class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square inerits from Rectangle
    """

    def __init__(self, size):
        """
            initiaitazation
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
            square area
        """
        return self.__size * self.__size

    def __str__(self):
        """
            __str__ magic function
        """
        return "[{}] {}/{}".format("Rectangle",
                                   self.__size, self.__size)
