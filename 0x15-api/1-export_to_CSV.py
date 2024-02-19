#!/usr/bin/python3
"""commentttttttttttttttttttttttttttttttt"""
import csv
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
        csv_file_name = f'{user}.csv'
        user_range = ((user - 1) * 20)
        with open(csv_file_name, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for row in tasks_data[user_range:user_range + 20]:
                resls = [
                    row['userId'],
                    user_data['username'],
                    row['completed'],
                    row['title']]
                writer.writerow(resls)
