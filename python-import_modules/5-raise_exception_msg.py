#!/usr/bin/env python3
def raise_exception_msg():
    user_input = input("Enter a custom message for the NameError: ")
    raise NameError(user_input)

try:
    raise_exception_msg()
except NameError as ne:
    print(ne)
