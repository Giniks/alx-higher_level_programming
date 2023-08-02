#!/usr/bin/python3
"""Defines the class square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """initualises the new square.

        Args:
            size (int): The size of the new square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integwr")
        elif size < 0:
            raise ValuseError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current area of the square."""
        return (self.__size * self.__size)
