#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys."""
    for keys_sot in sorted(a_dictionary.keys_sot()):
        print('{}: {}'.format(keys_sot, a_dictionary[keyy_sot]))
