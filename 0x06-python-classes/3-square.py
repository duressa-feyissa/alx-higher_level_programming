#!/usr/bin/python3
""" Module contains empty class Square """


class Square:
    """ This is an empty class. """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")


    def area(self):
        return self.__size * self.__size
