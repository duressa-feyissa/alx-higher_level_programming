#!/usr/bin/python3

def multiple_returns(sentence):
    new_tuple = ""
    if sentence is None:
        return new_tuple[0]
    new_tuple = (len(sentence), sentence[0])
    return new_tuple
