#!/usr/bin/python3
"""
    a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as req:
        print("Body response:")
        html = req.read()
        print("{}- type: {}".format("\t", type(html)))
        print("{}- content: {}".format("\t", html))
        print("{}- utf8 content: {}".format("\t", html.decode("UTF-8")))
