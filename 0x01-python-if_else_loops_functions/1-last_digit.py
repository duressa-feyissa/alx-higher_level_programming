#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

hold = "and is less than 6 and not 0"
hold1 = "and is greater than 5"
if number >= 0:
    x = number % 10
else:
    x = ((number * -1) % 10) * -1

if x == 0:
    print("Last digit of {0:d} is {1:d} and is 0".format(number, x))
else:
    if x > 5:
        print("Last digit of {0:d} is {1:d} {2:s}".format(number, x, hold1))
    else:
        print("Last digit of {0:d} is {1:d} {2:s}".format(number, x, hold))
