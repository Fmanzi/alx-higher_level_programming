#!/usr/bin/python3
"""A funt to add args to py list and save to a file"""

import sys
import os

if __name__ == "__main__":
    filename = "add_item.json"

    # Check if the file exists, if not, create an empty list
    if not os.path.exists(filename):
        my_list = []
    else:
        my_list = load_from_json_file(filename)

    # Add arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(my_list, filename)
