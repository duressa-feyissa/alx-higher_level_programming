#!/usr/bin/python3
"""
    contains class Rectangle which implements Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle implements Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the instance of the class..
        """

        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        else:
            if width <= 0:
                raise ValueError("width must be > 0")
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        else:
            if height <= 0:
                raise ValueError("height must be > 0")
            self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        else:
            if x < 0:
                raise ValueError("x must be > 0")
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        else:
            if y < 0:
                raise ValueError("y must be > 0")
            self.__y = y

        @property
        def width(self):
            """
            getter function
            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            setter function.
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            else:
                if value <= 0:
                    raise ValueError("width must be > 0")
                self.__width = value

        @property
        def height(self):
            """
            getter function
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            setter function.
            """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            else:
                if value <= 0:
                    raise ValueError("height must be > 0")
                self.__height = value

        @property
        def x(self):
            """
            getter function
            """
            return self.__x

        @x.setter
        def x(self, value):
            """
            setter function.
            """
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            else:
                if value < 0:
                    raise ValueError("x must be > 0")
                self.__x = value

        @property
        def y(self):
            """
            getter function
            """
            return self.__y

        @y.setter
        def y(self, value):
            """
            setter function.
            """
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            else:
                if value < 0:
                    raise ValueError("y must be > 0")
                self.__y = value

        def area(self):
            """
            Area function
            """
            return self.__width * self.__height

        def display(self):
            """
            Display function.
            """
            print("\n" * (self.__y), end="")
            for i in range(self.__height):
                if self.__x == 0:
                    print("#" * (self.__width - 1))
                else:
                    print(" " * (self.__x - 1), "#" * (self.__width - 1))


        def __str__(self):
            """
            str function
            """
            return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                    self.id ,self.__x,
                                                    self.__y, self.__width,
                                                    self.__height)

        def update(self, *args, **kwargs):
            """
            update function
            """
            if len(args) != 0:
                for i in range(len(args)):
                    if i == 0:
                        self.id = args[i]
                    elif i == 1:
                        self.width = args[i]
                    elif i == 2:
                        self.height = args[i]
                    elif i == 3:
                        self.x = args[i]
                    elif i == 4:
                        self.y = args[i]
                    else:
                        raise IndexError()
                else:
                    for i in kwargs.keys():
                        if i == "id":
                            self.id = kwargs[i]
                            if i == "width":
                                self.width = kwargs[i]
                            if i == "height":
                                self.height = kwargs[i]
                            if i == "x":
                                self.x = kwargs[i]
                            if i == "y":
                                self.y = kwargs[i]

        def to_dictionary(self):
            """
            the dictionary repr of a rect
            """
            new = dict()
            new['x'] = getattr(self, "x")
            new['y'] = getattr(self, "y")
            new['id'] = getattr(self, "id")
            new['height'] = getattr(self, "height")
            new['width'] = getattr(self, "width")
            return new
