#!/usr/bin/python3
def print_combinations(start_digit, end_digit):
    for digit1 in range(start_digit, end_digit + 1):
        for digit2 in range(digit1 + 1, end_digit + 1):
            print("{}{}".format(digit1, digit2), end=", ")

def main():
    print_combinations(0, 9)

if __name__ == "__main__":
    main()
