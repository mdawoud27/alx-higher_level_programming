#!/usr/bin/python3
"""Module doc string"""


def add_attribute(object, key, value):
    """add_attribute function doc string"""
    if not hasattr(object, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(object, key, value)
