#!/usr/bin/python3
"""This module defines a Rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """initialize a new rectangle

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def self(width):
        """Get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise
        TypeError('width must be an integer')
        if value < 0:
            raise
        ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the new rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise
        TypeError('height must be an integer')
        if value < o:
            raise
        ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.__width = 0 or self.__height = 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))