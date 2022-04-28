#!/usr/bin/python3
'''comment'''
import requests
from sys import argv
''' comment '''
if __name__ == "__main__":
    '''comment'''
    url = argv[1]
    page = requests.get(url)
    print(page.headers.get("X-Request-Id"))
