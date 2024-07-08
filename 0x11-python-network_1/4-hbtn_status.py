#!/usr/bin/python3
""" A python script that fetches https://alx-intranet.hbtn.io/status 
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    body = requests.get(url)
    print("Body Response:")
    print("\t- type: {}".format(type(body.text)))
    print("\t- content: {}".format(body.text))
