#!/usr/bin/python3
"""fetch the number of subscribers for a particular subreddit"""
import requests


def number_of_subscribers(subreddit) -> int:
    """returns the number of subs for a subreddit
    Args:
        subreddit(string): the fetch focus
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    result = requests.get(url, allow_redirects=False)
    about = result.json()
    if about is None:
        return 0
    about = about.get('data')
    subs = about.get('subscribers')
    return subs
