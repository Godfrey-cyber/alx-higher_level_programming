#!/usr/bin/python3
"""
    This Module contains add_integer function.
    whicn function returns two integers.
    5 line module comment.
"""


def add_integer(a, b=98):
    """sum up two integers and return the result.
    Args:
        a (int): The first integer.
        b (int): The secodn integer.
    """
    if type(a) is not int:
        if type(a) is float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return (a + b)
