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
