#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """Prevent user from creating instances from a new locked class attribute
    For anything but for attribute called 'First name".
    """

    __slot__ = ["first_name"]
