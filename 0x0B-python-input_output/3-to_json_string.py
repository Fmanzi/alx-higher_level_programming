#!/usr/bin/python3

"""A funct that returns a JSON representation of an str"""
import json

def to_json_string(my_obj):
    """Return the JSON representation of an object as a string"""
    return json.dumps(my_obj)

