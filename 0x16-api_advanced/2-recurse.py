#!/usr/bin/python3
"""API script"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches titles of hot articles for a given subreddit."""
    if subreddit is None:
        return None

    h = {'User-Agent': 'MyRedditApp/1.0 (by /u/YourRedditUsername)'}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after} if after else {'limit': 100}
    res = requests.get(url, headers=h, params=params, allow_redirects=False)

    if res.status_code != 200:
        return None

    try:
        data = res.json()
        children = data.get('data', {}).get('children', [])

        titles = [child['data']['title'] for child in children]
        hot_list.extend(titles)

        after = data['data'].get('after')
        if after:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list

    except ValueError as e:
        return None
