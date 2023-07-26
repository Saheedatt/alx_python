#!/usr/bin/env python3
def raise_exception_msg(message=""):
    raise NameError(message)

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
