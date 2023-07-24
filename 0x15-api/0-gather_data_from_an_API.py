#!/usr/bin/python3
"""get data from https://jsonplaceholder.typicode.com/"""
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    completed = 0
    completed_titles = []
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
        .format(user_id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    todos = requests.get(todos_url)
    user = requests.get(user_url)
    # users are employees and todos are tasks in this context
    employee_name = user.json().get('name')
    for task in todos.json():
        if task.get('completed'):
            completed += 1
            completed_titles.append(task.get('title'))
    total_tasks = len(todos.json())
    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                     completed, total_tasks))
    for title in completed_titles:
        print('\t {}'.format(title))
