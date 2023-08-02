#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class.

    Paramters:
    obj: Any- The object to check.
    a_class: class - The specified class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class or its subclass; otherwise, False.
    """
    current_class = type(obj)
    while current_class is not object:
        if current_class is a_class:
            return True
        current_class = current_class.__base__
    return False
