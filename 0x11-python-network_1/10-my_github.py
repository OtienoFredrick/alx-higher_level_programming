#!/usr/bin/python3
"""The script takes my github account credentials
    (username and password) and uses github API to dispay key
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r= requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))

