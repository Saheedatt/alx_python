#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

print(fibonacci_sequence(6))

print(fibonacci_sequence(1))

print(fibonacci_sequence(0))

print(fibonacci_sequence(20))
