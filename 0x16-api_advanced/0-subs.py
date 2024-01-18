#!/usr/bin/python3
"""API script"""
import requests


def number_of_subscribers(subreddit):
    """return total number of subscriber for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'alx-api/0.1 (by u/elghafiani)'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    json = res.json()
    if json["data"].get("subscribers"):
        return json["data"].get("subscribers")
    else:
        return 0
