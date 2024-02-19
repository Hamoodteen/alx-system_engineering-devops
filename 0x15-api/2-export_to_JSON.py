#!/usr/bin/python3
"""commentttttttttttttttttttttttttttttttt"""
import json
import requests
import sys


if __name__ == "__main__":
    user = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(f'{url}{user}')

    if response.status_code == 200:
        user_data = response.json()
        tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
        tasks_data = tasks.json()
        json_file_name = f'{user}.json'
        user_range = ((user - 1) * 20)
        resls = {user: []}
        for row in tasks_data[user_range:user_range + 20]:
            resls[user].append(row)
        with open(json_file_name, 'w', newline='') as file:
            json.dump(resls, file)
        with open(json_file_name, "r") as json_file:
            data = json.load(json_file)
        for item in data[str(user)]:
            item.pop("userId")
            item.pop("id")
            item["task"] = item.pop("title")
            item["completed"] = item.pop("completed")
            item["username"] = user_data["username"]
        with open(json_file_name, "w") as json_file:
            json.dump(data, json_file)
