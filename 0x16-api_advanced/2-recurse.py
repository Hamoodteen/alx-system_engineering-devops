#!/usr/bin/python3
"""commentttttttttttttttttttttttttttttttt"""
import requests


def recurse(subreddit, hot_list=[]):
    def nothing(ls):
        ls = None
        return ls
    nothing(hot_list)
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, params={'limit': 10})
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts == []:
            print(None)
        else:
            for post in posts:
                post_data = post['data']
                print(post_data["title"])
