#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenTuple1 = len(tuple_a)
    lenTuple2 = len(tuple_b)
    sum1 = 0
    sum2 = 0
    if lenTuple1 >= 2:
        sum1 += tuple_a[0]
        sum2 += tuple_a[1]
    if lenTuple2 >= 2:
        sum1 += tuple_b[0]
        sum2 += tuple_b[1]
    if lenTuple1 == 1:
        sum1 += tuple_a[0]
    if lenTuple2 == 1:
        sum1 += tuple_b[0]
    new_tuple = (sum1, sum2)
    return new_tuple
