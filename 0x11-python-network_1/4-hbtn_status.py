#!/usr/bin/python3
'''comment'''
import requests
''' comment '''
if __name__ == "__main__":
    '''comment'''
    url = "https://intranet.hbtn.io/status"
    req = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
