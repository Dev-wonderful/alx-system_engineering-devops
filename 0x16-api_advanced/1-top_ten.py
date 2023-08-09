#!/usr/bin/python3
"""fetch the top 10 posts for a particular subreddit"""
import requests


def top_ten(subreddit):
    """prints the top 10 posts title for a subreddit
    Args:
        subreddit(string): the fetch focus
    """
    header = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    params = {
        "limit": 10
    }
    url = f'https://www.reddit.com/r/{subreddit}/top.json'
    result = requests.get(url, allow_redirects=False,
                          headers=header, params=params)
    top_posts = result.json().get('data', None)
    if top_posts is None:
        print(None)
        return
    posts = top_posts.get('children', None)
    if len(posts) == 0:
        print(None)
        return
    for post in posts:
        title = post.get('data', None).get('title', None)
        print(title)
