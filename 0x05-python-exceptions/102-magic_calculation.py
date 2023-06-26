#!/usr/bin/python3


def magic_calculation(a, b):
    result_cal = 0
    for z in range(1, 3):
        try:
            if z > a:
                raise Exception('Too far')
            else:
                result_cal += (a ** b) / z
        except Exception:
            result_cal = b + a
            break
    return (result_cal)
