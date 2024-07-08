#!/usr/bin/python3
"""A python script that takes in a url
and displays the value of the variable X-request-Id in the 
response header"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
