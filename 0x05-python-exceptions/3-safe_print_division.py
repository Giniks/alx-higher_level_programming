#!/usr/bin/python3

def safe_print_division(a, b):
    """divides 2 integer and print the result.

    Args:
        a: Nominator.
        b: Denominator.

    Returns:
        The value of division otherwise none.
    """
    
    try:
        div = a/b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("inside result: {}".format(div))
    return (div)
