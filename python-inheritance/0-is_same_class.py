#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Parameters:
        obj: Any - The object to check.
        a_class: class - The given class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified
        class; otherwise return False.
    """
    return type(obj) is a_class
