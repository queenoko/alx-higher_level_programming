#!/usr/bin/python3
"""
Function module that indents texts
"""


def text_indentation(text):
    """This function prints a text with 2 new lines after each ".", "?", or ":"
    Arg:
    text (str): Print string
    Raises:
    TypeError: If text is not string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count_string = 0
    while count_string < len(text) and text[count_string] == " ":
        count_string = count_string + 1

    while count_string < len(text):
        print(text[count_string], end="")
        if text[count_string] == "\n" or text[count_string] in ".?:":
            if text[count_string] in ".?:":
                print("\n")
            count_string = count_string + 1
            while count_string < len(text) and text[count_string] == " ":
                count_string = count_string + 1
            continue
        count_string = count_string + 1
