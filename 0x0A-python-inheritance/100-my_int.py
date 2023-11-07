#!/usr/bin/python3
class MyInt(int):
    """Rebel integer class with inverted equality operators."""

    def __eq__(self, other):
        """Override equality operator (==) to invert the result."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override inequality operator (!=) to invert the result."""
        return super().__eq__(other)

