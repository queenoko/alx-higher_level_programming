#!/usr/bin/python3
"""function that writes an Object to text file, using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to text file using JSON """
    with open(filename, "w") as fil:
        json.dump(my_obj, fil)
