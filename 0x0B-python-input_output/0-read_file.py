#!/usr/bin/python3
"""Defines a function for reading text files"""

def read_file(filename=""):
    """Read and print the content of a text file"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())

