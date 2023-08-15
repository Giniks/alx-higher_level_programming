#!/usr/bin/python3
"""This module defines a BaseGeometry"""


class BaseGeometry:
    """Represents  BaseGeometry"""

    def area(self):
        """it is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this validates integers in form of parameter

        Args:
            name (str): The name of the parameter
            value (int): The parameter to validates
        Raises:
            TypeError: if the value is not integer
            ValueError: if value <= 0
        """
        if type(value) != int:
            raise TypeError("[] must be an integer".format(name))
        if value is <= 0:
            raise ValueError("[] must be greater than 0.format(name))
