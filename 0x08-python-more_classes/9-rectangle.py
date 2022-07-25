#!/usr/bin/python3
""" Module contains empty class Rectangle """


class Rectangle:
    """ class """

    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initilaizier """

        """ to set it """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        """ to set it """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        type(self).number_of_instances += 1

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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    def area(self):
        """ area """
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ str """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            string += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        return f"Rectangle({eval(repr(self.__width))}, \
{eval(repr(self.__height))})"

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        Area_1 = rect_1.area()
        Area_2 = rect_2.area()

        if Area_1 > Area_2:
            return rect_1
        elif Area_2 > Area_1:
            return rect_2
        else:
            return rect_1
