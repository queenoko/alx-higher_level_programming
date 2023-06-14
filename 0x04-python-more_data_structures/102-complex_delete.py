#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ deletes keys with a specific value in a dictionary."""
    delete_key = []
    for key_d in a_dictionary:
        if a_dictionary[key_d] == value:
            delete_key.append(key_d)
    for key_d in delete_key:
        del a_dictionary[key_d]
    return a_dictionary
