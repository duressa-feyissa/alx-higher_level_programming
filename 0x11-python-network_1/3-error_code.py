#!/usr/bin/python3
"""
    a Python script that takes in a URL, sends a request to the URL 
    and displays the body of the response
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    req = urllib.request.urlopen(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            html = res.read()
            print(html.decode("UTF-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
