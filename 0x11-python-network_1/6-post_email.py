#!/usr/bin/python3
"""
    sends a POST
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    value = {'email': argv[2]}
    print(requests.post(argv[1], data=value).text)
