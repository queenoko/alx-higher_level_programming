#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    else:
        maxi_integer = my_list[0]
        for z in range(len(my_list)):
            if my_list[z] > maxi_integer:
                maxi_integer = my_list[z]
        return (maxi_integer)
