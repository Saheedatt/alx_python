#!/usr/bin/env python3
def raise_exception():
    try:
        raise TypeError("This is a type exception!")
    except TypeError:
        print("Exception has been raised")

raise_exception()
