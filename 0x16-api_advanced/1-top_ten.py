#!/usr/bin/python3
"""commentttttttttttttttttttttttttttttttt"""
import requests


def top_ten(subreddit_name):
    url = f'https://www.reddit.com/r/{subreddit_name}/hot.json'
    response = requests.get(url, params={'limit': 10})
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts == []:
            print(None)
        else :
            for post in posts:
                post_data = post['data']
                print(post_data["title"])
