#!/usr/bin/python3
"""commentttttttttttttttttttttttttttttttt"""
import requests


def number_of_subscribers(subreddit_name):
    url = f'https://www.reddit.com/r/{subreddit_name}/about.json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
