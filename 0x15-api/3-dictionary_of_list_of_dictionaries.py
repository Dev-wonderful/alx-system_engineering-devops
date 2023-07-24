#!/usr/bin/python3
"""get data from https://jsonplaceholder.typicode.com/"""
import json
import requests


if __name__ == '__main__':
    users_url = 'https://jsonplaceholder.typicode.com/users'
    filename = 'todo_all_employees.json'
    todo_all_employees = {}

    def get_employee_tasks(url, username):
        todos = requests.get(url)
        tasks = todos.json()
        employee_tasks = []

        for task in tasks:
            task_dict = {
                'username': username,
                'task': task.get('title'),
                'completed': task.get('completed'),
            }
            employee_tasks.append(task_dict)
        return employee_tasks

    # hitting the endpoint
    # users are employees and todos are tasks in this context
    users = requests.get(users_url)
    employees = users.json()
    for employee in employees:
        employee_username = employee.get('username')
        employee_id = employee.get('id')
        todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos' \
            .format(employee_id)
        employee_data = get_employee_tasks(todos_url, employee_username)
        todo_all_employees[employee_id] = employee_data

    # write to file
    with open(filename, 'w', encoding='UTF8') as file:
        json.dump(todo_all_employees, file)
