#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides 2 integer and print the result.

    Args:
        a (int): Nominator.
        b (int): Denominator.

    Returns:
        The value of division otherwise none.
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("inside result: {}".format(div))
    return (div)
