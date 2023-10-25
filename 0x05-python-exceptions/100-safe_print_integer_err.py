#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        value_as_int = int(value)
        print("{:d}".format(value_as_int))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
