#!/usr/bin/env python3
def raise_exception():
    raise TypeError("This is a type exception!")

try:
    raise_exception()
except TypeError :
    print("Exception has been raised")
