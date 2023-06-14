#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys."""
    [print("{}: {}".format(q, a_dictionary[q])) for q in sorted(a_dictionary)]
