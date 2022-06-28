#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    print(f"{number} is positive")
else:
    if number == 0:
        print("{0:d} is zero".format(number))
    else:
        print("{0:d} is negative".format(number))
