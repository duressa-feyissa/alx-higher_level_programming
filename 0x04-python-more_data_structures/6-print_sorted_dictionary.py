#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    x = []
    for i in a_dictionary.keys():
        x.append(i)
    x.sort()
    for i in x:
        if i in a_dictionary.keys():
            print(i, ":", a_dictionary.get(i))
