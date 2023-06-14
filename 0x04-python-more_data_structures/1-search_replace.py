#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list."""
    def search_find(item):
        return item if item != search else replace
    return list(map(search_find, my_list))
