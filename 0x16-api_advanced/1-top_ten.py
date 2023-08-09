#!/usr/bin/python3
"""fetch the number of subscribers for a particular subreddit"""
import requests


def top_ten(subreddit) -> int:
    """returns the number of subs for a subreddit
    Args:
        subreddit(string): the fetch focus
    """
    header = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    url = f'https://www.reddit.com/r/{subreddit}/top.json?limit=10'
    result = requests.get(url, allow_redirects=False, headers=header)
    top_posts = result.json().get('data', None)
    if top_posts is None:
        return 0
    posts = top_posts.get('children', None)
    for post in posts:
        title = post.get('data', None).get('title', None)
        print(title)
