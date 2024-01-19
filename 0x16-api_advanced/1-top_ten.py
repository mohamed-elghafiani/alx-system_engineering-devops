#!/usr/bin/python3
"""API script"""
import requests


def top_ten(subreddit):
    """return total number of subscriber for a subreddit"""
    url = "https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit)
    headers = {'User-Agent': 'alx-api-12345/0.1 (by u/elghafiani)'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    data = res.json()["data"]["children"]
    for post in data[:10]:
        print(post["data"]["title"])
