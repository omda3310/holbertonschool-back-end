#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def first_line(id):
    """ Fetch number of tasks """

    todos_count = 0
    todos_done = 0
    done_list = []

    resp_user = requests.get(users_url)
    resp = requests.get(todos_url).json()

    if resp_user.status_code == 200 and resp.status_code == 200:
        us_ok = resp_user.json()
        todo_ok = resp.json()
        if not us_ok or not todo_ok:
            print("error")
    name = None
    for j in resp_user:
        if j[id] == id:
            name = j[id]

    for i in resp:
        if i['userId'] == id:
            todos_count += 1
        if (i['completed'] and i['userId'] == id):
            todos_done += 1
            done_list.append(i.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        name, todos_done, todos_count))
    for done in done_list:
        print("\t {}: OK".format(done.get('title')))


if __name__ == "__main__":
    first_line(int(sys.argv[1]))
