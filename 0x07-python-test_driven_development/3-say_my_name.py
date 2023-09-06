#!/usr/bin/python3
"""Module doc string."""


def say_my_name(first_name, last_name=""):
    """Function prints the name.

    Args:
        first_name (string): Person first name.
        last_name (string): Person last name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
