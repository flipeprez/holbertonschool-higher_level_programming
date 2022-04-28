#!/usr/bin/python3
'''comment'''
from urllib import request, parse
from sys import argv
''' comment '''
if __name__ == "__main__":
    '''comment'''
    email = argv[2]
    my_email_dict = {
    "email": email
}
    data = parse.urlencode(my_email_dict).encode()
    page = request.Request(argv [1], data=data)
    with request.urlopen(page) as pages:
         f = pages.read()    
         print(f.decode("utf-8"))
