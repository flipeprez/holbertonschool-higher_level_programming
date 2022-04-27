#!/usr/bin/python3
'''comment'''
import urllib.request
from sys import argv


if __name__ == "__main__":
    '''comment'''
    url = argv [1]
    try:
        with urllib.request.urlopen(url) as response:
            page = response.read()
            print(page.decode("utf-8"))
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
