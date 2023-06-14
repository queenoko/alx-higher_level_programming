#!/usr/bin/python3

def roman_to_int(roman_string):
    """converts roman numerals to integer"""
    if not roman_string or type(roman_string) != str:
        return 0
    total_r = 0
    digit_r = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for roman_r in reversed(roman_string):
        arabic_r = digit_r[roman_r]
        total_r += arabic_r if total_r < arabic_r * 5 else -arabic_r
    return total_r
