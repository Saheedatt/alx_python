#!/usr/bin/python3
def  is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class.

    Paramters:
    obj: Any- The object to check.
    a_class: class - The specified class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class or its subclass; otherwise, False.
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
