#!/usr/bin/python3
'''comment'''
import urllib.request
from sys import argv
''' comment '''
if __name__ == "__main__":
    '''comment'''
    url = argv [1]
    with urllib.request.urlopen(url) as response:
        page = response.headers.get("X-Request-Id")
        print(page)
