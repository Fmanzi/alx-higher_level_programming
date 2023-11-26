#!/usr/bin/python3
"""Defines an inherites class list"""

class MyList(list):
     """Inherits from list and provides a method to print sorted list."""
    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))

