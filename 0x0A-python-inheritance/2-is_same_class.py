#!/usr/bin/python3
"""This defines same class checking function"""

def is_same_class(obj, a_class):
    """This checks if the object is an instance of same class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of object

        Returns: True if the object is exactly an instance of the class.
        Otherwise False.
    """
    if type (obj) == a_class:
        return True
    return False
