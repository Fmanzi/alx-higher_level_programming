#!/usr/bin/python3
def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible, otherwise raise a TypeError."""
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")

