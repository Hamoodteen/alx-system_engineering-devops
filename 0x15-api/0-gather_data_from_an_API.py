#!/usr/bin/python3
"""commentttttttttttttttttttttttttttttttt"""
import requests
import sys


if __name__ == "__main__":
    user = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(f'{url}{user}')

    if response.status_code == 200:
        done = 0
        done_list = []
        user_data = response.json()
        tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
        tasks_data = tasks.json()
        user_range = ((user - 1) * 20)
        for i in range(user_range, user_range + 20):
            if tasks_data[i]['completed']:
                done += 1
                done_list.append(f"     {tasks_data[i]['title']}")
        print(f"Employee {user_data['name']} is done with tasks({done}/20):")
        print(*done_list, sep="\n")
