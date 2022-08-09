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
                    new[x] = args[x]
        self.__init__(new[1], new[2], new[3], new[4], new[0])

    def to_dictionary(self):
        """the dictionary repr of a rect
        """
        new = dict()
        new['id'] = self.id
        new['size'] = self.size
        new['x'] = self.x
        new['y'] = self.y
        return new
