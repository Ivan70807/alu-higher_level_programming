#!/usr/bin/python3
"""
Module providing a function to check for inherited instance matches.
"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited from a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
