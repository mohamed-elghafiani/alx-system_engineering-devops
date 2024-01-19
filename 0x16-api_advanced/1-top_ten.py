#!/usr/bin/python3
"""API script"""
import requests


def top_ten(subreddit):
    """return top 10 hot posts for a subreddit"""
    h = {'User-Agent': 'MYAPP/1.0 (by /u/elghafiani)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    res = requests.get(url, headers=h, allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    data = res.json()["data"]["children"]
    for post in data[:10]:
        print(post["data"]["title"])
