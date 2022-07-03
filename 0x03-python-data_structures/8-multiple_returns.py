#!/usr/bin/python3

def multiple_returns(sentence):
    new_tuple = (0, None)
    if sentence is None:
        return new_tuple
    new_tuple = (len(sentence), sentence[0])
    return new_tuple
