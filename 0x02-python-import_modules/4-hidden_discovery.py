#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    hold = dir(hidden_4)
    for x in hold:
        if x[0:2] != "__":
            print(x)
