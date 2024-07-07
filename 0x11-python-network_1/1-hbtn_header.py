#!/usr/bin/python3
""" A python script that takes in a URL, sends in a request to the url, and disolays 
the value of the X request-id variable found in the header of the response"""

import urllib.request
import sys

if "__name__" == "__main__":
    url = sys.argv[1]
    requests = urllib.request.Request(url)
    with urllib.request.urlopen() as response:
        print(dict(response.headers).get("X-Request-id"))
