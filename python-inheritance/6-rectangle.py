#!/usr/bin/python3
class BaseGeometry:
    """
    This is a class representing the base geometry.

    It can be used as a base class to create other geometry-related classes.

    Attributes:
        None

    Methods:
        area(self):Raises an Exception with the message "area() is not implemented".
        integer_validator(self, name, value): Validates the value as an integer and raises exceptions if invalid.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".

        This method needs to be implemented in the subclass to calculate
        the area of the specific geometry.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer and raises exceptions if invalid.

        Parameters:
            name (str): The name of the value to be validated.
            value: The value to be validated.

        Raises:
            TypeError, if the value is not an integer.
            ValueError, if the value is <= 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This class represents a Rectangle.

    It inherits from the BaseGeometry class.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError, if width or height is not an integer.
            ValueError, ff width or height is <=.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
