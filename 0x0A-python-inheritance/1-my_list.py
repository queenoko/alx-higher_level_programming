#!/usr/bin/python3
"""class MyList inherits fron list """


class MyList(list):
    """parent class list is inherited"""
    def print_sorted(self):
        """returns sorted list"""
        print(sorted(self))
