#!/usr/bin/python3

class Square:
     """Defines a square with a size attribute.

    Args:
        size (int): The size of the square.

    Attributes:
        __size (int): The size of the square.

    """
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        """int: Retrieve the size of the square."""
        return self.__size
