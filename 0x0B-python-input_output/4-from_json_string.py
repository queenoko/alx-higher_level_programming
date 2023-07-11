#!/usr/bin/python3
"""function that returns object, represents JSON string
of python data structure"""


import json


def from_json_string(my_str):
    """Returns Python object  which represents JSON string"""
    return json.loads(my_str)
