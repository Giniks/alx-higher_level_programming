#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: pointer to a function to execute
        args: Arguments for fct.

    Returns:
        The result of the function.
        otherwise, return None and prints stderr preceded by Exception.
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
