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

    check = ['+', '-', '*', '/']
    if op not in check:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if op == '+':
        print("{0:d} {1:s} {2:d} = {3:d}".format(a, op, b, a + b))
    if op == '-':
        print("{0:d} {1:s} {2:d} = {3:d}".format(a, op, b, a - b))
    if op == '*':
        print("{0:d} {1:s} {2:d} = {3:d}".format(a, op, b, a * b))
    if op == '/':
        print("{0:d} {1:s} {2:d} = {3:d}".format(a, op, b, a / b))
