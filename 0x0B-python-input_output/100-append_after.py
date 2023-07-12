#!/usr/bin/python3
"""function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """appends text after each line containing a given string in file"""
    text1 = ""
    with open(filename) as fil:
        for line in fil:
            text1 += line
            if search_string in line:
                text1 += new_string
    with open(filename, "w") as wri:
        wri.write(text1)
