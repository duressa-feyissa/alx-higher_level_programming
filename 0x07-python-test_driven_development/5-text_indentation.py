#!/usr/bin/python3
"""
    text_indentation

"""


def text_indentation(text):
    """
        text_indentation() - a function that prints a text with 2 new
        lines after each of these characters: ., ? and :

        Args:
            text - string
        Void

    """
    count = 1
    if type(text) is not str:
        raise TypeError("text must be a string")

    hold = ""
    for i in text:
        if i is "." or i is "?" or i is ":":
            hold = hold + i
            count = 0
        else:
            hold = hold + i
        if count == 0:
            print(hold.strip())
            print("")
            hold = ""
            count = 1
    print(hold.strip(), end="")
