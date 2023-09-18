#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class doc string."""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constractor."""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ magic function."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Return the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size value of the square.

        Args:
            value (int): new size value.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Function that assidn attrs.

        Args:
            args (tuple): args.
            kwargs (dictionary): dictionary.
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
