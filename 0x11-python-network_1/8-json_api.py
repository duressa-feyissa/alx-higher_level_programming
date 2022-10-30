#!/usr/bin/python3
"""
script to take in a URL input, sends a request to the URL, display response
"""


if __name__ == '__main__':
    from sys import argv
    import requests

    url = "http://0.0.0.0:5000/search_user"
    value = {'q': ""}
    try:
        value['q'] = argv[1]
    except IndexError:
        print('No result')
    else:
        req = requests.post(url, data=value)
        try:
            out = req.json()
            if out:
                print('[{}] {}'.format(out['id'], out['name']))
            else:
                print('No result')
        except requests.exceptions.RequestException:
            print('Not a valid JSON')
