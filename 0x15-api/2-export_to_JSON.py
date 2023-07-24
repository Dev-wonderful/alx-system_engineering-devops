#!/usr/bin/python3
"""get data from https://jsonplaceholder.typicode.com/"""
import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
        .format(user_id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    filename = f'{user_id}.json'
    employee_tasks = []

    # hitting the endpoint
    todos = requests.get(todos_url)
    user = requests.get(user_url)

    # users are employees and todos are tasks in this context
    user = user.json()
    employee_username = user.get('username')
    tasks = todos.json()

    for task in tasks:
        task_dict = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': employee_username
        }
        employee_tasks.append(task_dict)
    employee_data = {user_id: employee_tasks}

    # writing to file
    with open(filename, 'w', encoding='UTF8') as file:
        json.dump(employee_data, file)
