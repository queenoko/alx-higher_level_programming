#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    """Divide two lists element by element

    Arg:
    my_list1 (list): First list
    My_list2 (list): Second list
    list_length (int): Number of element to divide.

    Reteun:
    A new lent list containing all division
    """

    fresh_list = []
    for z in range(0, list_length):
        try:
            divi = my_list_1[z] / my_list_2[z]
        except TypeError:
            print("wrong type")
            divi = 0
        except ZeroDivisionError:
            print("division by 0")
            divi = 0
        finally:
            fresh_list.append(divi)
        return (fresh_list)
