#!/usr/bin/env python3
def raise_exception_msg(message=""):
    if not isinstance(message, str):
        raise TypeError("Message should be a string")
    if message.lower() == "python is cool":
        raise NameError("NameError: Python is cool")
    elif message.lower() == "c is fun":
        raise NameError("NameError: C is fun")
    elif message.lower() == "":
        raise NameError("NameError: No message provided")
    else:
        raise NameError("NameError: " + message)

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

try:
    raise_exception_msg("Python is cool")
except NameError as ne:
    print(ne)

try:
    raise_exception_msg("")
except NameError as ne:
    print(ne)
