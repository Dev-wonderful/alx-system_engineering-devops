#!/usr/bin/python3
"""get data from https://jsonplaceholder.typicode.com/"""
import csv
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    titles = []
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
        .format(user_id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    filename = f'{user_id}.csv'

    # hitting the endpoint
    todos = requests.get(todos_url)
    user = requests.get(user_url)

    # users are employees and todos are tasks in this context
    user = user.json()
    employee_username = user.get('username')
    todos = todos.json()

    # writing to file
    with open(filename, 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            task_completed_status = task.get('completed')
            task_title = task.get('title')
            writer.writerow([user_id, employee_username,
                             task_completed_status, task_title])
