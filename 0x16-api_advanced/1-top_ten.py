#!/usr/bin/python3
"""
Function that queries the reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """
    Function that queries the reddit api
    -if not a valid subrredit, print None
    """
    req = requests.get(
            "https://www.reddit.com/r/{}/hot.json".format(subreddit),
            headers={"User-Agent": "Custom"},
            params={"limit": 10},
            )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
