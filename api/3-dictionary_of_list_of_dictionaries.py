#!/usr/bin/python3
"""
This script uses the JSON placeholder API to query data about an employee.
"""
import json
import requests
URL = 'https://jsonplaceholder.typicode.com'


def get_users():
    """Fetch user by ID."""
    resp = requests.get(f'{URL}/users')
    resp.raise_for_status()
    return resp.json()


def get_todos(id):
    """Fetch TODO and return ID"""
    resp = requests.get(f'{URL}/todos', params={'userId': user_id})
    resp.raise_for_status()
    todos = resp.json()
    return todos


def export_all_to_json():
    """Export alll to json"""
    all_data = {}

    try:
        users = get_users()
        for user in users:
            user_id = user['id']
            username = user['username']
            todos = get_todos(user_id)

            task_list = []
            for t in todos:
                t_data = {
                    "username": username,
                    "task": t['title'],
                    "completed": t['completed']
                }
                task_list.append(t_data)

            all_data[str(user_id)] = task_list

        with open("todo_all_employees.json", "w") as json_file:
            json.dump(all_data, json_file)

    except requests.RequestException as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    export_all_to_json()
