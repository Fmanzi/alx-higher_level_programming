#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    results = []

    for num in my_list:
        is_divisible = num % 2 == 0
        results.append(is_divisible)
    return results
