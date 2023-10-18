#!/usr/bin/python3
"""
This script uses the JSON placeholder API to query data about an employee.
"""

import requests
from sys import argv
URL = 'https://jsonplaceholder.typicode.com'


def get_name(user_id):
    """Fetch user by ID."""
    resp = requests.get(f"{URL}/users/{id}")
    resp.raise_for_status()
    user_name = resp.json()
    return user_name.get('name')


def get_todos(id):
    """Fetch TODO and return ID"""
    resp = requests.get(f"{URL}/todos", params={'userId': id})
    resp.raise_for_status()
    todos = resp.json()
    return todos


def display_infos(id):
    try:
        user_name = get_name(id)
        todos = get_todos(id)
        num_todos = len(todos)
        completed_todos = [t for t in todos if t.get("completed")]
        print("Employee {} is done with tasks({}/{}):".format(
            user_name, len(completed_todos), num_todos))
        for t in completed_todos:
            print(f"\t {t['title']}")
    except requests.RequestException as ex:
        print(f"Error: {ex}")


if __name__ == '__main__':
    if len(argv) < 2:
        exit(1)
    user_id = int(argv[1])
    display_infos(user_id)
