#!/usr/bin/python3

def safe_print_integer(value):
    """print an integer with "{:d}".format().

    Args:
        value (int): The inter value to be printed.

    Returns:
        True if value printed is integer.
        Otherwise it returns false.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
