#!/usr/bin/python3
""" class Rectangle that defines a rectangle
"""


class Rectangle:
    """ class Rectangle"""
    def __init__(self, width=0, height=0):
        """ Instantiated with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """defining width
        """
        return self.__width

    @property
    def height(self):
        """defining height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
