#!/usr/bin/python3
"""
    1-my_list.py: print_sorted()
"""


class MyList(list):
    """
        a class MyList that inherits from list
    """

    def print_sorted(self):
        """
            prints the list, but sorted (ascending sort)
        """

        hold = list(map(lambda x: x, self))
        hold.sort()
        print(hold)
