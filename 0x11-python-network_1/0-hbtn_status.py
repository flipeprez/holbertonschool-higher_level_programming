#!/usr/bin/python3
'''comment'''
from urllib.request import Request, urlopen
''' comment '''
if __name__ == "__main__":
    '''comment'''
    url = "https://intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as response:
        page = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))
    print("\t- utf8 content: {}".format(page.decode("utf-8")))
