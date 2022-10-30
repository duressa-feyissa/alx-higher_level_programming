#!/usr/bin/python3
"""
    sends a POST
"""


if __name__ == '__main__':
    import requests
    sys import srgv

    value = {'email': argv[2]}
    res = requests.post(argv[1], data=value)
    print(res.text)
