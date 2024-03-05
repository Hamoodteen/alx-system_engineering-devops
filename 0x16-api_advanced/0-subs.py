#!/usr/bin/python3
"""commentttttttttttttttttttttttttttttttt"""
import requests


def get_subreddit_subscribers(subreddit_name):
    url = f'https://www.reddit.com/r/{subreddit_name}/about.json'
    headers = {'User-Agent': 'your_user_agent_here'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return None
