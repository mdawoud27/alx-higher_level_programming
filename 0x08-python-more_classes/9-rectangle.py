#!/usr/bin/python3

"""This is a define of Rectangle."""


class Rectangle:
    """Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initalize the rectangle.

        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return the width value."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle width

        Args:
            value (int): rectangle width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle height.

        Args:
            value (int): Rectangle new height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return: Rectangle area."""
        return self.__height * self.__width

    def perimeter(self):
        """Return: Rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """__str__ magic function"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)


    def __repr__(self):
        """__repr__ magic function"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """__del__ magic func"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Function that compares between rectangles.

        Args:
            rect_1: Instance of Rectangle.
            rect_2: Instance of Rectangle.

        Return:
            The biggest rectangle based on the area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
