#!/usr/bin/python3
"""
This script uses the JSON placeholder API to query data about an employee.
"""

import csv
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


def display_infos(id):
    """Display details"""
    try:
        user_name = get_name(id)
        todos = get_todos(id)
        num_todos = len(todos)
        completed_todos = [t for t in todos if t['completed']]
        print(f"Employee {user_name} is done with"
              f"tasks({completed_todos}/{num_todos}):")
        for t in completed_todos:
            print(f"\t {t['title']}")
    except requests.RequestException as e:
        print(f"Error: {e}")


def export_to_csv(id):
    """export"""
    try:
        user_infos = requests.get(f"{URL}/users/{id}").json()
        user_name = user_infos.get('username')
        todos = get_todos(id)

        with open(f"{id}.csv", "w", newline='') as csv_file:
            fieldnames = [
                "USER_ID",
                "USERNAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"
            ]
            writer = csv.DictWriter(
                csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            for t in todos:
                writer.writerow({
                    "USER_ID": id,
                    "USERNAME": user_name,
                    "TASK_COMPLETED_STATUS": t['completed'],
                    "TASK_TITLE": t['title']
                })

    except requests.RequestException as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    if len(argv) < 2:
        exit(1)
    user_id = int(argv[1])
    export_to_csv(user_id)
