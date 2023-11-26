#!/usr/bin/python3
"""Program that defines an obj lookup functions """

def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return (dir(obj))
