#!/usr/bin/python3
"""Takes in a url and an email adress sends 
a Post request to the passed url"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
