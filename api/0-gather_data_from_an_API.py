#!/usr/bin/python3
"""
This script uses the JSON placeholder API to query data about an employee.
"""

import requests
from sys import argv

URL = 'https://jsonplaceholder.typicode.com'


def get_name(user_id):
    """Fetch user by ID."""
    resp = requests.get(f"{URL}/users/{user_id}")
    user_name = resp.json().get('name')
    return user_name


def get_todos(user_id):
    resp = requests.get(f"{URL}/todos", params={'userId': user_id})
    todos = resp.json()
    return todos


def display_infos(user_id):
    try:
        user_name = get_name(user_id)
        todos = get_todos(user_id)
        num_todos = len(todos)
        num_completed_todos = len([t for t in todos if t.get("completed")])
        print("Employee {} is done with tasks({}/{}):".format(
            user_name, num_completed_todos, num_todos))
        for t in todos:
            if t.get("completed"):
                print(f"\t {t.get('title')}")
    except requests.RequestException as ex:
        print(f"Error: {ex}")


if __name__ == '__main__':
    if len(argv) < 2:
        exit(1)
    user_id = int(argv[1])
    display_infos(user_id)
