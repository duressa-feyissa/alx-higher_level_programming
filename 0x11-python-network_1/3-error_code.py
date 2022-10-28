#!/usr/bin/python3
"""
    a Python script that takes in a URL, sends a request to the URL 
    and displays the body of the response
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            html = req.read()
            print(html.decode("UTF-8"))
    except urllib.error.HTTPError:
        print("Error code: {}".format(res.code))
