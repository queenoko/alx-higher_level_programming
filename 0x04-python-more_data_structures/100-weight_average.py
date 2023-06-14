#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num_w = 0
        ave_w = 0
        for tup_w in my_list:
            num_w += (tup_w[0] * tup_w[1])
            ave_w += (tup_w[1])
        return (num_w/ave_w)
    return 0
