#!/usr/bin/python3
"""Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle Class
    Args:
        size, x=0, y=0, id=None
    Raisses:
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Intialization
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation
        """

        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self._Rectangle__x,
                                                 self._Rectangle__y,
                                                 self._Rectangle__width)

    @property
    def size(self):
        """size getter
        """
        return self._Rectangle__width

    @size.setter
    def size(self, size):
        """ size getter
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the Rectangle.
         Args:
             *args (ints): New attribute values.
             **kwargs (dict): New key/value pairs of attributes.
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
        """the dictionary repr of a rect
        """
        new = dict()
        new['id'] = self.id
        new['width'] = self.width
        new['height'] = self.height
        new['x'] = self.x
        new['y'] = self.y
        return new
