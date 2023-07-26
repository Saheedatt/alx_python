#!/usr/bin/env python3
def raise_exception_msg(message=""):
    raise NameError(message)

try:
    custom_message = input("Enter a custom message for the NameError: ")
    raise_exception_msg(custom_message)
except NameError as ne:
    print(ne)
