#!/usr/bin/python3
class BaseGeometry:
    """
    This is an empty class representing the base geometry.

    It can be used as a base class to create other geometry-related classes.

    Attributes:
        None

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented".
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".

        This method needs to be implemented in the subclass to calculate the
        area of the specific geometry.
        """
        raise Exception("area() is not implemented")
