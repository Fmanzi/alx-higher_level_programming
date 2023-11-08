#!/usr/bin/python3
"""A function that returns an obj rep of an str"""

import json

def from_json_string(my_str):
    """Return an object represented by a JSON string"""
    return json.loads(my_str)

