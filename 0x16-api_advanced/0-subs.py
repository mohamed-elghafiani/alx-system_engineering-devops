#!/usr/bin/python3
"""API script"""
import requests


def number_of_subscribers(subreddit):
    """return total number of subscriber for a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'alx-api-12345/0.1 (by u/elghafiani)'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    json = res.json()
    if json["data"].get("subscribers"):
        return json["data"].get("subscribers")
    else:
        return 0
