#!/usr/bin/python3
for number in range(100):
    if number < 10:
        print("0{:02}".format(number), end=", ")
    else:
        print("{:02}".format(number), end=", ")

print()
