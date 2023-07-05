#!/usr/bin/python3
""""
Function module that prints firstname and lastname
"""


def say_my_name(first_name, last_name=""):
    """Function that prints name (<first name> <last name>)

    Arg:
    first_name (str): Prints first name
    last_name (str): prints last name

    Raises:
    TypeError: If first_name or last_name are not strings

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
