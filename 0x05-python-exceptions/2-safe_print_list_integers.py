#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x interger element of a list.

    Args:
        my_list (list): the list to print the element from.
        x (int): The number of element to access in my list.

    Returns:
        The real number of integers printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
