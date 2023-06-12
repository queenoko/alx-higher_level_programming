#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    my_div_list = []

    for z in my_list:
        if z % 2 == 0:
            my_div_list.append(True)
        else:
            my_div_list.append(False)
    return (my_div_list)
