#!/usr/bin/python3
"""function that appends a file"""


def append_write(filename="", text=""):
    """Appends string to end of UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as fil:
        return fil.write(text)
