#!/usr/bin/python3
"""A funct that creates an obj from a json file"""

import json

def load_from_json_file(filename):
    """Create an object from a JSON file"""
    with open(filename, 'r') as file:
        return json.load(file)

