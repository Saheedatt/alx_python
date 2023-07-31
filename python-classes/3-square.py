#!/usr/bin/python3
"""
This module defines the Square class, which represents a square shape.

Square:
    A class to create and manipulate square objects.

"""

class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of the square.
    Methods:
        __init__(self, size=0): Initializes a Square instance with a given size (default is 0).
        area(self): Calculate and return the area of the square.
        my_print(self): Print the square pattern using '#'.
    """
    def __init__(self, size = 0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (default is 0).
        """
        self._size = size
    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self._size
    @size.setter
    def size(self, value):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value
    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._size **2
