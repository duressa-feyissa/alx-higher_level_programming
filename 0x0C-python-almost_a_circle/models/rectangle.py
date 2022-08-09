#!/usr/bin/python3
# rectangle.py
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: chaeck type.
            ValueError: Check value
        """

        # Validate variable  width
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        # validate variable height
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        # validate variable x
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        # validate varaible y
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter
        """

        return self.__width

    @width.setter
    def width(self, width):
        """width setter
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter
        """

        return self.__height

    @height.setter
    def height(self, height):
        """height setter
        """

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter
        """

        return self.__x

    @x.setter
    def x(self, x):
        """x setter
        """

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter
        """

        return self.__y

    @y.setter
    def y(self, y):
        """y setter
        """

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of the current rectangle
        """

        return self.__width * self.__height

    def display(self):
        """prints the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            print()
            return

        if self.__y != 0:
            print("\n" * (self.__y - 1))
        for y in range(self.__height):
            if self.__x != 0:
                print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """string representaaion of the class
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Update the Rectangle.
         Args:
             *args (ints): New attribute values.
             **kwargs (dict): New key/value pairs of attributes.
        """

        new = [self.id, self.__width, self.__height, self.__x, self.__y]
        if len(args) == 0 or args is None:
            if len(kwargs) == 0:
                return
            else:
                try:
                    new[0] = kwargs['id']
                except KeyError:
                    pass
                try:
                    new[1] = kwargs['width']
                except KeyError:
                    pass
                try:
                    new[2] = kwargs['height']
                except KeyError:
                    pass
                try:
                    new[3] = kwargs['x']
                except KeyError:
                    pass
                try:
                    new[4] = kwargs['y']
                except KeyError:
                    pass
        else:
            for x in range(len(args)):
                if x < len(new):
                    new_args[x] = args[x]
        self.__init__(new[1], new[2], new[3], new[4], new[0])

    def to_dictionary(self):
        """the dictionary repr of a rect
        """
        new = dict()
        new['id'] = self.id
        new['width'] = self.width
        new['height'] = self.height
        new['x'] = self.x
        new['y'] = self.y
        return new
