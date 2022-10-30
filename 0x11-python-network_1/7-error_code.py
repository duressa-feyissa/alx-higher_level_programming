#!/usr/bin/python3
"""
    sends a request to the URL, display response
"""


if __name__ == '__main__':
    from sys import argv
    import requests

    try:
        res = requests.get(argv[1])
        print(res.content.decode('utf-8'))
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.code))

        
