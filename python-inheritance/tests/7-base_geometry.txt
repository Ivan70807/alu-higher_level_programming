#!/usr/bin/python3
"""
Module defining the BaseGeometry class.
"""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """
        Raises an Exception indicating area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value as an integer greater than 0.

        Args:
            name (str): The name associated with the value.
            value (int): The value to be validated.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
