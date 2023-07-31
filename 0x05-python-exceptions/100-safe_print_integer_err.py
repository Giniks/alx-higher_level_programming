#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """prints an integer value.

    Args:
        value (int); The value integer to be printed.

    Returns:
        True if the value integer has been correctly printed.
        otherwise, false and prints with stderr preceded by Exception.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
