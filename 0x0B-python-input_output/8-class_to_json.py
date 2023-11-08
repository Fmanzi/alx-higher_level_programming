#!/usr/bin/python3
"""Defines a py class to JSON funct"""

def class_to_json(obj):
    """Return a dictionary representation of an object for JSON serialization"""
    return obj.__dict__

