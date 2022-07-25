#!/usr/bin/python3
import sys


if len(sys.argv) != 2:
	print("Usage: nqueens N")
	sys.exit(1)

if sys.argv[1].isdigit() is False:
	print("N must be a number")
	sys.exit(1)

num = int(sys.argv[1])
if num < 4:
	print("N must be at least 4")
	sys.exit(1)
