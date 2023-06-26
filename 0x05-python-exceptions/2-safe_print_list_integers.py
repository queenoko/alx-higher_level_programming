#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    """prints first x element of a list that are integers

    Arg:
    my-LIST (LIST): the list to print elements from
    x (int: The number of the element of my_list to print

    Return:
    printed number of elements
    """

    retun = 0
    for z in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            retun += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (retun)
