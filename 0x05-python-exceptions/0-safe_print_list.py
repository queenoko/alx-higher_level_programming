#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints x element of a list.
    Arg:
    my_list (list): Its the list to print elements from x int:
    The number of elements of my_list to print
    Return: Number of element printed
    """

    retun = 0
    for z in range(x):
        try:
            print("{}".format(my_list[z]), end="")
            retun += 1
        except IndexError:
            break
    print("")
    return (retun)
