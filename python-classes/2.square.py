#!/usr/bin/python3
class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of the square.
    """
        
    def __init__(self, size = 0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (default is 0).
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._size **2
    