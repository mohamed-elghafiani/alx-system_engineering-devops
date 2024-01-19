#!/usr/bin/python3
"""API script"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches titles of hot articles for a given subreddit."""
    if subreddit is None:
        return None

    headers = {'User-Agent': 'MyRedditApp/1.0 (by /u/YourRedditUsername)'}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after} if after else {'limit': 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()
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
