#!/usr/bin/python3
a = 1
b = 2

# Importing the add function from add_0.py
from add_0 import add as FAKE_add

print("{} + {} = {}".format(a, b, FAKE_add(a, b)))
