#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == '__main__':
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if op == '+':
        print("{0:d} + {1:d} = {2:d}".format(a, b, a + b))
    elif op == '-':
        print("{0:d} - {1:d} = {2:d}".format(a, b, a - b))
    elif op == '*':
        print("{0:d} * {1:d} = {2:d}".format(a, b, a * b))
    elif op == '/':
        print("{0:d} / {1:d} = {2}".format(a, b, a / b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
