#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

import json
import requests
from sys import argv
URL = 'https://jsonplaceholder.typicode.com'


def get_name(id):
    """fetch user by Id"""
    resp = requests.get(URL + "/users/{}".format(id))
    user_infos = resp.json()
    return user_infos.get('name')


def get_todos(id):
    resp = requests.get(URL + "/todos", params={'userId': id})
    todo_infos = resp.json()
    return todo_infos


def display_infos(id):
    name = get_name(id)
    todo = get_todos(id)
    todo_num = len(todo)
    todo_complete = len([t for t in todo
                         if t.get("completed")])
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todo_complete, todo_num))
    for t in todo:
        if (t.get("completed")):
            print("\t {}".format(t.get("title")))


if __name__ == '__main__':
    if len(argv) < 2:
        exit(1)
    id = int(argv[1])
    display_infos(id)
