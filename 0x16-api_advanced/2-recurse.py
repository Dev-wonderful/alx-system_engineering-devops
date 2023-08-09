#!/usr/bin/python3
"""fetch all hot posts for a particular subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """return all hot posts title for a subreddit
    Args:
        subreddit(string): the fetch focus
        hot_list(list): contains a list of titles
        after(string): result listing next button
    """
    header = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    params = {
        'after': after,
        'limit': 100
    }
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    result = requests.get(url, allow_redirects=False,
                          headers=header, params=params)
    all_posts = result.json().get('data', None)
    if all_posts is None:
        return None
    posts = all_posts.get('children', None)
    if len(posts) == 0:
        return None
    for post in posts:
        title = post.get('data', None).get('title', None)
        hot_list.append(title)
    if all_posts.get('after') is not None:
        after_str = all_posts.get('after')
        hot_result = recurse(subreddit, hot_list, after=after_str)
        if hot_result is not None:
            hot_list = hot_result
        return hot_list
    else:
        return None
