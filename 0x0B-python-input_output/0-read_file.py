#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Prints UTF8 text file content"""
    with open(filename, encoding="utf-8") as fil:
        print(fil.read(), end="")
