#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    MAX = None
    for i in a_dictionary.values():
        if MAX is None or MAX < i:
            MAX = i
    key_list = list(a_dictionary.keys())
    val_list = list(a_dictionary.values())
    index = val_list.index(MAX)
    return key_list[index]
