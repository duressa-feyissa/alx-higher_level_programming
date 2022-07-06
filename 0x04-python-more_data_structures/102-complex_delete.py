#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = []
    for name in a_dictionary:
        if a_dictionary[name] is value:
            key.append(name)
    if key is None:
        return a_dictionary
    for i in key:
        a_dictionary.pop(i)
    return a_dictionary
