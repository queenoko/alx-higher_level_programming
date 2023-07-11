#!/usr/bin/python3
"""function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates a Python object from JSON file"""
    with open(filename) as fil:
        return json.load(fil)
