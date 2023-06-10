#!/usr/bin/python3

def no_c(my_string):
    new_word = ''
    for z in my_string:
        if z != 'c' and z != 'C':
            new_word += z
        return(new_word)
