#!/usr/bin/python3
"""Defines a locked class"""

class LockedClass:
    """Prevent users from creating instances from a new locked class attributes.
    For anything but for attribute called 'First name".
    """

    __slot__ = ["first_name"]
