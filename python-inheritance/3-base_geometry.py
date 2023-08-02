#!/usr/bin/python3

"""
This module defines a function to check if object is exactly an instance of a specified class.

Function:
    is_same_class(obj, a_class): Checks if object is exactly an instance of the specified class.

"""


class BaseGeometry:
    """
    This is an empty class representing our base geometry.

    It can be used as a base class to create other geometry-related classes.

    Attributes:
        None

    Methods:
        None
    """
    def __init__(self):
        """
        Initialize a BaseGeometry object.
        """
        pass

    def __repr__(self):
        """
        Return a string representation of the geometric object.

        Returns:
            A string representation of the geometric object.
        """
        return f"BaseGeometry()"
