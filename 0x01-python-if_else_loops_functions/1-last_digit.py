#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_r = abs(number) % 10
if number < 0:
    num_r = -num_r
print("Last digit of {} is {} and is ".format(number, num_r), end="")
if num_r > 5:
    print("greater than 5")
elif num_r == 0:
    print("0")
else:
    print("less than 6 and not 0")
