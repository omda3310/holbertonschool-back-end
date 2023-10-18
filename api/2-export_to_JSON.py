#!/usr/bin/python3
"""
This script uses the JSON placeholder API to query data about an employee.
"""

import json
import requests
from sys import argv
URL = 'https://jsonplaceholder.typicode.com'


def get_name(id):
    """Fetch user by ID."""
    resp = requests.get(f'{URL}/users/{id}')
    resp.raise_for_status()
    user_name = resp.json()
    return user_name.get('name')


def get_todos(id):
    """Fetch TODO and return ID"""
    resp = requests.get(f'{URL}/todos', params={'userId': id})
    resp.raise_for_status()
    todos = resp.json()
    return todos


def export_to_json(id):
    """Export to json"""
    try:
        employee_username = get_name(id)
        todos = get_todos(id)

        task_list = []
        for t in todos:
            t_data = {
                "task": t['title'],
                "completed": t['completed'],
                "username": employee_username
            }
            task_list.append(t_data)

        json_structure = {str(id): task_list}
        with open(f"{id}.json", "w") as json_file:
            json.dump(json_structure, json_file)

    except requests.RequestException as e:
        print(f"An error occured: {e}")


if __name__ == '__main__':
    if len(argv) < 2:
        exit(1)
    user_id = int(argv[1])
    export_to_json(user_id)

