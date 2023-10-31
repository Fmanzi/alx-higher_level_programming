#!/usr/bin/python3

class Rectangle:
    """
    This is the Rectangle class.
    It defines a rectangle with private attributes: width and height.
    """
    
    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.
        Args:
            width (int, optional): The width of the rectangle. Default is 0.
            height (int, optional): The height of the rectangle. Default is 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.
        Args:
            value (int): The new width to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.
        Args:
            value (int): The new height to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

