#!/usr/bin/python3

def no_c(my_string):
    new_word = ''
    for z in my_string:
        if z != 'C' and z != 'c':
            new_word += z
        return(new_word)
