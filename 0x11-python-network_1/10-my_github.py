#!/usr/bin/python3
"""
- uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
