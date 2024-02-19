#!/usr/bin/python3
"""commentttttttttttttttttttttttttttttttt"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(f'{url}')

    if response.status_code == 200:
        user_data = response.json()
        tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
        tasks_data = tasks.json()
        json_file_name = "todo_all_employees.json"
        resls = {
            1: [], 2: [], 3: [], 4: [], 5: [],
            6: [], 7: [], 8: [], 9: [], 10: []}
        for i in range(1, 11):
            for row in tasks_data[(i - 1) * 20:((i - 1) * 20) + 20]:
                resls[i].append(row)
        with open(json_file_name, 'w', newline='') as file:
            json.dump(resls, file)
        with open(json_file_name, "r") as json_file:
            data = json.load(json_file)
        for i in range(1, 11):
            for item in data[str(i)]:
                item.pop("userId")
                item.pop("id")
                item["username"] = user_data[i - 1]["username"]
                item["task"] = item.pop("title")
                item["completed"] = item.pop("completed")
        with open(json_file_name, "w") as json_file:
            json.dump(data, json_file)
