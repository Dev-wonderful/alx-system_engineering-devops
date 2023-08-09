#!/usr/bin/python3
"""fetch the number of subscribers for a particular subreddit"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subs for a subreddit
    Args:
        subreddit(string): the fetch focus
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    result = requests.get(url)
    about = result.json()
    subs = about.get('data').get('subscribers')
    return subs
