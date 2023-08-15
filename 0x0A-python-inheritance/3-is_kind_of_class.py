#!/usr/bin/python3
"""This module checks both the class and inherited class chexking function."""


def is_kind_of_class(obj, a_class):
    """this checks if the class object us the instance of the inherited class

    Args:
        obj (any): The objecy to check.
        a_class (type): The type of class to match the object

    Returns:
          True if the object is an instance
          otherwise False
    """

    if isinstance(obj, a_class):
        return True
    return False
