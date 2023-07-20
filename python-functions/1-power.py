#!/usr/bin/env python3

def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        a = 1 / a
        b = -b
    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2
    return result
