#!/usr/bin/python3

for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        print("{:d}{:d}".format(first_digit, second_digit), end=', ' if first_digit < 9 and second_digit < 8 else '\n')
