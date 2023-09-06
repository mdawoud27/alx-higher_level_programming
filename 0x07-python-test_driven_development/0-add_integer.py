#!/usr/bin/python3
"""Module doc string"""


def add_integer(a, b=98):
    """Function that adds 2 integers.
    Args:
        a (int), b (int): Integer values.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
