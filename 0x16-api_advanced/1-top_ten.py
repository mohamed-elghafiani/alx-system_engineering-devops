#!/usr/bin/python3
"""API script"""
import requests


def top_ten(subreddit):
    """return top 10 hot posts for a subreddit"""
    h = {'User-Agent': 'MYAPP/1.0 (by /u/elghafiani)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 10, 'after': after} if after else {'limit': 10}
    res = requests.get(url, headers=h, params=params, allow_redirects=False)
    data = res.json()["data"]["children"]
    for post in data:
        print(post["data"]["title"])
