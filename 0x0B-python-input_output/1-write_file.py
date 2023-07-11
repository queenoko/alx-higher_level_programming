#!/usr/bin/python3
"""writes a string to a text file """


def write_file(filename="", text=""):
    """Writes string to UTF8 text file
    """
    with open(filename, "w", encoding="utf-8") as fil:
        return fil.write(text)
