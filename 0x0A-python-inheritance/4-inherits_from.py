#!/usr/bin/python3
"""This defines an inherited class"""

def inherits_from(obj, a_class):
    """Determines if an object is from inherited class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

        Returns: True  if obj is instance of an inherites class
        otgerwise false. 
    """
    if issubclass(type(obj), a_class) and type obj != a_class:
        return True
    return False
